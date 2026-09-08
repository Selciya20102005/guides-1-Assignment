import frappe


def update_context(context):

    context.system_name = "Student Management System"

    context.total_students = frappe.db.count(
        "Student"
    )