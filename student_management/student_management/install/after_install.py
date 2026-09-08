import frappe


def after_install():

    frappe.logger().info("Student Management App Installed Successfully")

    print("After Install Hook Executed")