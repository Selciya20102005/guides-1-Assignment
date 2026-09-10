# Copyright (c) 2026, selciya and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Student Name"),
            "fieldname": "student_name",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": _("Email"),
            "fieldname": "student_email",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": _("Department"),
            "fieldname": "department",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": _("Batch"),
            "fieldname": "batch",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("Grade"),
            "fieldname": "grade",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": _("CGPA"),
            "fieldname": "cgpa",
            "fieldtype": "Float",
            "width": 100,
        },
    ]


def get_data(filters=None):
    filters = filters or {}

    conditions = {}

    if filters.get("department"):
        conditions["department"] = filters["department"]

    return frappe.get_all(
        "Student",
        fields=[
            "student_name",
            "student_email",
            "department",
            "batch",
            "grade",
            "cgpa",
        ],
        filters=conditions,
        order_by="student_name asc",
    )