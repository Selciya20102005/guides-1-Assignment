import frappe


def after_migrate():

    print("After Migrate Hook Executed")

    frappe.logger().info("Migration completed successfully.")