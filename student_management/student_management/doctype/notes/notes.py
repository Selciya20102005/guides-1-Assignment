# Copyright (c) 2026, selciya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Notes(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		content: DF.Text | None
		id: DF.Data | None
	# end: auto-generated types

	pass
