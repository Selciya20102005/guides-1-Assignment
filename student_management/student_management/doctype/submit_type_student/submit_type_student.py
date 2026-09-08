# Copyright (c) 2026, selciya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class submittypestudent(Document):
	def before_submit(self):
		if self.fees_paid<5000:
			frappe.throw("Pay the full amount")

	def before_cancel(self):
		if self.course_completion=="completed":
			frappe.throw("cannot cancel after completion")

	def before_update_after_submit(self):
		if self.has_value_changed("department"):
			frappe.throw("cannot edit the department")

	def on_submit(self):
		self.db_set("status","Approved")

	def on_cancel(self):
		self.db_set("status","Not approved")

	def on_update_after_submit(self):
		frappe.msgprint("Submitted document updated successfully")