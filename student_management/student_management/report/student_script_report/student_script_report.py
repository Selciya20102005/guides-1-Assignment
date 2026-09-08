import frappe
from frappe import _


def execute(filters=None):

    columns = get_columns()
    data = get_data()

    return columns, data


def get_columns():

    return [
        {
            "label": _("Student Name"),
            "fieldname": "student_name",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": _("Email"),
            "fieldname": "student_email",
            "fieldtype": "Data",
            "width": 220,
        },
        {
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Batch"),
            "fieldname": "batch",
            "fieldtype": "Int",
            "width": 80,
        },
        {
            "label": _("Grade"),
            "fieldname": "grade",
            "fieldtype": "Float",
            "width": 80,
        },
        {
            "label": _("CGPA"),
            "fieldname": "cgpa",
            "fieldtype": "Float",
            "width": 80,
        },
    ]


def get_data():

    return frappe.get_all(
        "Student",
        fields=[
            "student_name",
            "student_email",
            "department",
            "batch",
            "grade",
            "cgpa"
        ]
    )