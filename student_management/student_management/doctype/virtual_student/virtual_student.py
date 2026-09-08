import frappe
import json
import os
from frappe.model.document import Document


def get_file_path():
    return os.path.join(os.path.dirname(__file__), "students.json")


def get_students():
    file_path = get_file_path()
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)


def save_students(students):
    file_path = get_file_path()
    with open(file_path, "w") as f:
        json.dump(students, f, indent=2)


def generate_name(students):
    """Generate next STU-XXXX id"""
    if not students:
        return "STU-0001"
    numbers = []
    for s in students:
        try:
            numbers.append(int(s["name"].split("-")[1]))
        except (IndexError, ValueError):
            continue
    next_num = (max(numbers) + 1) if numbers else 1
    return f"STU-{next_num:04d}"


class VirtualStudent(Document):

    def db_insert(self, *args, **kwargs):
        students = get_students()

        if not self.name:
            self.name = generate_name(students)

        # prevent duplicate name
        if any(s.get("name") == self.name for s in students):
            frappe.throw(f"Student {self.name} already exists")

        record = {
            "name": self.name,
            "student_roll_no": self.student_roll_no,
            "student_name": self.student_name,
            "department": self.department,
            "cgpa": self.cgpa,
        }

        students.append(record)
        save_students(students)

    def load_from_db(self):
        students = get_students()
        student = next(
            (s for s in students if s.get("name") == self.name), None
        )
        if not student:
            frappe.throw(f"Student {self.name} not found")
        super(Document, self).__init__(student)

    def db_update(self, *args, **kwargs):
        students = get_students()
        found = False

        for i, s in enumerate(students):
            if s.get("name") == self.name:
                students[i] = {
                    "name": self.name,
                    "student_roll_no": self.student_roll_no,
                    "student_name": self.student_name,
                    "department": self.department,
                    "cgpa": self.cgpa,
                }
                found = True
                break

        if not found:
            frappe.throw(f"Student {self.name} not found")

        save_students(students)

    def delete(self, *args, **kwargs):
        students = get_students()
        new_students = [s for s in students if s.get("name") != self.name]

        if len(new_students) == len(students):
            frappe.throw(f"Student {self.name} not found")

        save_students(new_students)

    @staticmethod
    def get_list(filters=None, page_length=20, **kwargs):
        students = get_students()

        if filters:
            for f in filters:
                # filters come as [doctype, fieldname, operator, value] or [fieldname, operator, value]
                if len(f) == 4:
                    _, key, operator, value = f
                else:
                    key, operator, value = f

                if operator == "=":
                    students = [s for s in students if s.get(key) == value]
                elif operator == "like":
                    val = str(value).replace("%", "").lower()
                    students = [
                        s for s in students
                        if val in str(s.get(key, "")).lower()
                    ]

        return students[:page_length]

    @staticmethod
    def get_count(filters=None, **kwargs):
        return len(get_students())

    @staticmethod
    def get_stats(**kwargs):
        return {}