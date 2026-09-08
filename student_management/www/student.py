import frappe


# allow_guest = True


# def get_context(context):

#     student_name = frappe.form_dict.student_name

#     student = frappe.get_doc(
#         "Student",
#         student_name
#     )

#     context.student = student



def get_context(context):

    student = frappe.get_doc(
        "Student",
        frappe.form_dict.student_name
    )

    context.student = student

    return context