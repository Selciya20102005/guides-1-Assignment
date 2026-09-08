import frappe


def after_sync():

    print("After Sync Hook Executed")

    frappe.logger().info("After Sync executed successfully.")