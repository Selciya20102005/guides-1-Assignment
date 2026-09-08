from frappe.desk.doctype.todo.todo import ToDo
import frappe


class CustomToDo(ToDo):

    def on_update(self):
        # Execute Frappe's original ToDo on_update()
        super().on_update()

        # Your custom logic
        frappe.msgprint("Custom ToDo on_update() executed!")