// Copyright (c) 2026, selciya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Transaction Test", {
// 	refresh(frm) {

// 	},
// });
frappe.call({
    method: "student_management.realtime_demo.show_progress_demo",

    callback: function(response) {
        console.log("Python method completed");
        console.log(response.message);
    }
});