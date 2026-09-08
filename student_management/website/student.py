import frappe


def extend_context(context):

    context.message = "Testing Extension"

    context.total_students = frappe.db.count(
        "Student"
    )

    return context