// Copyright (c) 2026, selciya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student ID details", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Student ID details", {
    refresh(frm) {
        frm.add_custom_button("Create Contact", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Create Contact",

                fields: [
                    {
                        label: "First Name",
                        fieldname: "first_name",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],

                primary_action_label: "Create Contact",

                primary_action(values) {
                    dialog.hide();

                    frappe.route_options = {
                        first_name: values.first_name
                    };

                    frappe.new_doc("Contact");
                }
            });

            dialog.show();
        });
    }
});