import frappe


@frappe.whitelist()
def get_cached_student_count():

    cached_count = frappe.cache().get_value("student_count")

    if cached_count is not None:
        return {
            "source": "cache",
            "count": cached_count
        }

    count = frappe.db.count("Student")

    frappe.cache().set_value(
        "student_count",
        count
    )

    return {
        "source": "database",
        "count": count
    }


def clear_cache():
    frappe.cache().delete_value("student_count")