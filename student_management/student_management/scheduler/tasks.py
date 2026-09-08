import frappe

def update_student_status():
    students = frappe.get_all(
        "Student",
        filters={"student_status": "Applied"}
    )

    for student in students:
        frappe.db.set_value(
            "Student",
            student.name,
            "student_status",
            "Approved"
        )

    frappe.db.commit()

print("Student status updated successfully.")