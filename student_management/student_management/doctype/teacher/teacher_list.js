console.log("TEACHER LIST JS FILE LOADED");

frappe.listview_settings['Teacher'] = {

    add_fields: [
        'status2',
        'student_group',
        'department',
        'student_name'
    ],
    //hide_name_filter: true,
    //hide_name_column: true,

    onload(listview) {

        // 1. Check the current route
        listview.page.add_inner_button("Check Current Route", () => {
            let route = frappe.get_route();
            console.log("Current Route:", route);
        });


        // 2. Route in parts
        // Navigate from Teacher List to a specific Teacher Form
        listview.page.add_inner_button("Route - Parts", () => {
            frappe.set_route("Form", "Teacher", "gayathri");
        });


        // 3. Route as an array
        // Navigate to the Student List
        listview.page.add_inner_button("Route - Array", () => {
            frappe.set_route(["List", "Student", "List"]);
        });


        // 4. Route as a string
        // Navigate to the Student List
        listview.page.add_inner_button("Route - String", () => {
            frappe.set_route("List/Student/List");
        });


        // 5. Route with options
        // Show only Teachers whose department is CSE
        listview.page.add_inner_button("Show CSE Teachers", () => {

            frappe.route_options = {
                department: "CSE"
            };

            frappe.set_route("List", "Teacher", "List");
        });
        // listview.page.add_inner_button("Test Format", () => {

        //     let date = frappe.format(
        //         "2019-09-08",
        //         { fieldtype: "Date" }
        //     );

        //     let amount = frappe.format(
        //         "2399",
        //         { fieldtype: "Currency" }
        //     );

        //     console.log("Formatted Date:", date);
        //     console.log("Formatted Amount:", amount);
        // });

    },
    // get_form_link(doc) {
    // return `/app/teacher-dashboard/${encodeURIComponent(doc.name)}`;
    // },

    // ---------------------------------------------------------
    // STATUS INDICATOR
    // ---------------------------------------------------------
    get_indicator(doc) {

        console.log(
            "TEACHER GET INDICATOR:",
            doc.name,
            doc.status2
        );

        if (doc.status2 === 'Active') {
            return [
                __('ok'),
                'yellow',
                'status2,=,Active'
            ];
        }

        if (doc.status2 === 'Inactive') {
            return [
                __('Inactive'),
                'red',
                'status2,=,Inactive'
            ];
        }

        return [
            __('Not Set'),
            'gray',
            'status2,is,not set'
        ];
    },

    // ---------------------------------------------------------
    // SINGLE BUTTON
    // ---------------------------------------------------------
    button: {

        show(doc) {
            return !!doc.student_group;
        },

        get_label() {
            return __('View Group');
        },

        get_description(doc) {
            return __('Open Student Group {0}', [
                doc.student_group
            ]);
        },

        action(doc) {

            frappe.set_route(
                'Form',
                'Student Group',
                doc.student_group
            );

        }
    },

    // ---------------------------------------------------------
    // DROPDOWN WITH MULTIPLE BUTTONS
    // ---------------------------------------------------------
    dropdown_button: {

        get_label: __('Actions'),

        buttons: [

            // -------------------------------------------------
            // 1. OPEN TEACHER
            // -------------------------------------------------
            {
                get_label: __('Open Teacher'),

                show(doc) {
                    return true;
                },

                get_description(doc) {
                    return __('Open Teacher {0}', [
                        doc.name
                    ]);
                },

                action(doc) {

                    frappe.set_route(
                        'Form',
                        'Teacher',
                        doc.name
                    );

                }
            },

            // -------------------------------------------------
            // 2. VIEW STUDENT GROUP
            // -------------------------------------------------
            {
                get_label: __('View Student Group'),

                show(doc) {
                    return !!doc.student_group;
                },

                get_description(doc) {
                    return __('Open Student Group {0}', [
                        doc.student_group
                    ]);
                },

                action(doc) {

                    frappe.set_route(
                        'Form',
                        'Student Group',
                        doc.student_group
                    );

                }
            },

            // -------------------------------------------------
            // 3. SHOW TEACHER DETAILS
            // -------------------------------------------------
            {
                get_label: __('Show Details'),

                show(doc) {
                    return true;
                },

                get_description(doc) {
                    return __('Show details for {0}', [
                        doc.name
                    ]);
                },

                action(doc) {

                    frappe.msgprint({
                        title: __('Teacher Details'),
                        message: `
                            <b>Teacher:</b>
                            ${frappe.utils.escape_html(doc.name || '-')}
                            <br><br>

                            <b>Teacher ID:</b>
                            ${frappe.utils.escape_html(doc.teacher_id || '-')}
                            <br><br>

                            <b>Department:</b>
                            ${frappe.utils.escape_html(doc.department || '-')}
                            <br><br>

                            <b>Student Group:</b>
                            ${frappe.utils.escape_html(doc.student_group || '-')}
                            <br><br>

                            <b>Status:</b>
                            ${frappe.utils.escape_html(doc.status2 || '-')}
                        `
                    });

                }
            }

        ]
    },

    // ---------------------------------------------------------
    // FORMATTERS
    // ---------------------------------------------------------
    formatters: {

        teacher_name(val) {
            return String(val || '').toUpperCase();
        }

    }

};