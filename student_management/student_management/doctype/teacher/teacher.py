# Copyright (c) 2026, selciya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Teacher(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from student_management.student_management.doctype.subjects.subjects import Subjects
		from student_management.student_management.doctype.teacher_student.teacher_student import TeacherStudent

		department: DF.Data | None
		joining_date: DF.Date | None
		student_handled: DF.Table[Subjects]
		student_name: DF.Link | None
		students: DF.TableMultiSelect[TeacherStudent]
		subjects_handles: DF.Table[Subjects]
		teacher_id: DF.Int
		teacher_name: DF.Data | None
	# end: auto-generated types

	pass
