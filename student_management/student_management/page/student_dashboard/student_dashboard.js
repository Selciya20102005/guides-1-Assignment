frappe.pages["student_dashboard"].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Student Dashboard",
        single_column: true
    });

    frappe.show_alert({
        message: "Student Dashboard Loaded!",
        indicator: "green"
    });

    console.log("Student Dashboard JS Loaded");

};