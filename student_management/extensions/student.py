import frappe

class StudentExtension:

    @property
    def student_info(self):
        return f"{self.student_name} - {self.department}"

    def custom_validation(self):
        frappe.msgprint("Mixin custom_validation() executed")

        if self.cgpa < 0:
            frappe.throw("CGPA cannot be negative")

    def validate(self):
        frappe.msgprint("Mixin validate() - before super")

        super().validate()

        frappe.msgprint("Mixin validate() - after super")

        self.custom_validation()