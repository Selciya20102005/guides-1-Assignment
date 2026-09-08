import frappe

# Assignment
@frappe.whitelist()
def teacher_department_api():

    Teacher = frappe.qb.DocType("Teacher")
    StudentDepartment = frappe.qb.DocType("Student Department")

    # Query Builder API
    query = (
        frappe.qb.from_(Teacher)
        .join(StudentDepartment)
        .on(Teacher.department == StudentDepartment.name)
        .select(
            Teacher.name,
            Teacher.teacher_id,
            Teacher.teacher_name,
            StudentDepartment.dept,
            StudentDepartment.dept_id
        )
        .limit(10)
    )

    results = query.run(as_dict=True)

    if not results:
        return []

    # Document API
    teacher = frappe.get_doc("Teacher", results[0]["name"])

    teacher.mark = 100

    teacher.save()

    # Database API
    for row in results:
        frappe.db.set_value(
            "Teacher",
            row["name"],
            "mark",
            100
        )

    # Remove internal document name from response
    for row in results:
        row.pop("name", None)

    return results











# @frappe.whitelist(allow_guest=True)
# def redact_student(email):

#     # Get all registered user_data_fields hooks
#     hooks = frappe.get_hooks("user_data_fields")

#     # Find the hook for Student doctype
#     hook = next(
#         h for h in hooks
#         if h.get("doctype") == "Student"
#     )

#     print("Student Hook:", hook)

#     # Find Student using the configured filter field
#     student = frappe.get_value(
#         "Student",
#         {
#             hook["filter_by"]: email
#         }
#     )

#     if not student:
#         return "Student Not Found"

#     # Load the document
#     doc = frappe.get_doc("Student", student)

#     # Redact all configured fields
#     for field in hook["redact_fields"]:
#         doc.set(field, "REDACTED")

#     doc.save(ignore_permissions=True)
#     frappe.db.commit()

    
#     return "Student Redacted Successfully"


# @frappe.whitelist()
# def custom_get(doctype, name):
#     frappe.msgprint("Custom get() Hook Executed!")

#     doc = frappe.get_doc(doctype, name)

#     return doc
