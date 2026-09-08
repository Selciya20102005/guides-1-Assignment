import frappe
import time


@frappe.whitelist()
def show_progress_demo():

    for i in range(1, 6):

        progress = i * 20

        frappe.publish_progress(
            progress,
            title="Student Management",
            description=f"Processing step {i} of 5"
        )

        time.sleep(1)

    return "Process completed"