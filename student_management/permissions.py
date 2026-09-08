import frappe

def student_has_permission(doc, user=None, permission_type=None):

    frappe.logger().info(f"User: {user}, Student User: {doc.user}")

    if user == "Administrator":
        return True

    if doc.user == user:
        return True

    return False