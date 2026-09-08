# Copyright (c) 2026, selciya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
import re
# from frappe.website.website_generator import WebsiteGenerator


class Student(Document):

    def before_insert(self):
        self.admission_date=frappe.utils.today()
        self.register_no=f"REG-{frappe.generate_hash(length=6)}"
        if not self.department:
            self.department="AI&DS"

    def before_naming(self):
        # if self.hostel_student:
        #     self.naming_series="HOSTEL-.YYYY.-.####"
        # else:
        #     self.naming_series="DAY-.YYYY.-.####"

        self.initial=self.student_name[0]

    def autoname(self):
        self.name=make_autoname(f"{self.initial}-{self.department}-A-.##")


    def before_validate(self):
        if not self.department:
            self.department="CSBS"
        if self.total_marks:
            self.percentage=(self.marks_obtained/self.total_marks)*100


    def validate(self):
        if self.hostel_student and self.day_scholar:
            frappe.throw("Student cannot be both Hostel Student and Day Scholar")

        if not frappe.db.exists("Student Department",self.department_name):
            frappe.throw("Enter the valid Department")

        mobile=re.sub(r"\D","",str(self.mobile_number))
        if len(mobile)!=12:
            frappe.throw("Enter valid mobile number")


        if frappe.db.exists("student",
            { "mobile_number":self.mobile_number,
             "name":["!=",self.name]
             }
             ):
             frappe.throw("mobile number already exists")



    def before_save(self):
        if not self.student_email:
            self.student_email=(
                f"{self.student_name.lower()}@gmail.com"
            )

    def after_insert(self):
        student_id=frappe.get_doc({
            "doctype":"Student ID details",
            "student":self.name,
            "status":"Active"
        })
        student_id.insert()

    def on_update(self):
        frappe.sendmail(
            recipients=self.student_email,
            subject="student record updation",
            message="updated Successfully"
        )

    #  def on_change(self):
    #     self.db_set("last_modified_time", now_datetime())

    # def approve(self):
    #     self.status = "Approved"

    #     self.add_comment(
    #         "Info",
    #         "Admission Approved"
    #     )

    #     self.save()


@frappe.whitelist()
def show_department(student_name):
    student = frappe.get_doc("Student", student_name)
    department = frappe.get_doc("Student Department", student.department)

    frappe.msgprint(f"Department: {department.dept}")