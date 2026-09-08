import frappe


def on_cancel(doc, method):

    cards = frappe.get_all(
        "Library Card",
        filters={"membership": doc.name},
        pluck="name"
    )

    for card in cards:
        card_doc = frappe.get_doc("Library Card", card)

        if card_doc.docstatus == 1:
            card_doc.cancel()