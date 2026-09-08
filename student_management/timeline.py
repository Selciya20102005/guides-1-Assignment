import frappe


def student_timeline(doctype, docname):

    student = frappe.get_doc(doctype, docname)

    if not student.interaction:
        return []

    return [
        {
            "creation": student.modified,
            "template": "my_custom_timeline",
            "template_data": {
                "message": student.interaction
            }
        }
    ]