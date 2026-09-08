import frappe

def before_install():
    print("Before Install Hook Executed")
    frappe.logger().info("Before Install executed successfully.")