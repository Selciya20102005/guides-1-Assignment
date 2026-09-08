import frappe
from frappe.utils import now


def get_timeline_data(doctype, docname):
    print("========== STUDENT TIMELINE HOOK ==========")
    print("DocType:", doctype)
    print("Document:", docname)

    return [
        {
            "creation": now(),
            "content": f"""
                <div>
                    <strong>Student Timeline Hook</strong>
                    <br>
                    Custom timeline entry for {docname}
                </div>
            """
        }
    ]