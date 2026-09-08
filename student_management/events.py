import frappe


def validate_tag(doc, method=None):
    if doc.name.lower() == "test":
        frappe.throw("The tag name 'test' is not allowed")