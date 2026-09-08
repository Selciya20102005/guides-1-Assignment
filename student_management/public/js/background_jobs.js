console.log("background_jobs.js loaded");

frappe.pages["rq-job"].on_page_show = function(wrapper) {

    console.log("RQ Job Page Shown");

    frappe.show_alert({
        message: "RQ Job Page Loaded!",
        indicator: "blue"
    });

};