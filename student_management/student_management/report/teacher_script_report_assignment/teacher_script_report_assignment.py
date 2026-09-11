import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Teacher Name",
            "fieldname": "teacher_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Department",
            "fieldname": "department",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Joining Date",
            "fieldname": "joining_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Salary",
            "fieldname": "salary",
            "fieldtype": "Currency",
            "width": 120
        }
    ]

    data = [
        {
            "teacher_name": "John Smith",
            "department": "Computer Science",
            "joining_date": "2024-01-15",
            "salary": 50000
        },
        {
            "teacher_name": "Priya Kumar",
            "department": "Electronics",
            "joining_date": "2023-08-20",
            "salary": 55000
        },
        {
            "teacher_name": "Rahul Sharma",
            "department": "Mechanical",
            "joining_date": "2022-06-10",
            "salary": 60000
        }
    ]

    return columns, data