import frappe

def generate_roll_number(doc, method):

    count = frappe.db.count("Student")

    doc.student_roll_no = f"ROLL{count + 1:03d}"