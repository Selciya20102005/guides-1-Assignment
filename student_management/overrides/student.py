import frappe

from student_management.student_management.doctype.student.student import Student


class CustomStudent(Student):

    def validate(self):
        frappe.msgprint("1. Before super")

        # super().validate()

        frappe.msgprint("3. After super")

        if self.cgpa < 0:
            frappe.throw("CGPA cannot be negative")