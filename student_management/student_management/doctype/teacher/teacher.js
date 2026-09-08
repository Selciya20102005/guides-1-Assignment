// Copyright (c) 2026, selciya and contributors
// For license information, please see license.txt



console.log("TEACHER JS LOADED");
frappe.ui.form.on("Teacher", {
    refresh(frm) {
        frm.add_custom_button("Create Task", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Create Task",

                fields: [
                    {
                        label: "Task Subject",
                        fieldname: "task_subject",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],

                primary_action_label: "Create Task",

                primary_action(values) {
                    frappe.call({
                        method: "student_management.task_api.create_task",
                        args: {
                            task_subject: values.task_subject
                        },
                        callback(response) {
                            dialog.hide();

                            frappe.msgprint({
                                title: "Success",
                                message: `Task ${response.message} created successfully.`,
                                indicator: "green"
                            });
                        }
                    });
                }
            });

            dialog.show();
        });
    }
});




// frappe.ui.form.on("Teacher", {
// 	refresh(frm) {

// 	},
// });
// frappe.realtime.on("my_test_event", (data) => {
//     console.log("Realtime event received!");
//     console.log(data);

//     frappe.msgprint(data.message);
// });

// frappe.call({
//     method: "student_management.api.test_realtime",
//     callback: function (response) {
//         console.log("Python method completed");
//         console.log(response.message);
//     }
// });
// frappe.ui.form.on("Teacher", {
//     refresh(frm) {

//         frm.add_custom_button("Load Students", () => {

//             frappe.require(
//                 "/assets/student_management/js/teacher_student.js",
//                 () => {

//                     TeacherStudents.show_students(frm);

//                 }
//             );

//         });
//     }
// });

// frappe.ui.form.on("Teacher", {
//     refresh(frm) {

//         frm.add_custom_button("Load Students", () => {

//             frappe.require(
//                 "/assets/student_management/js/teacher_student.js",
//                 () => {

//                     console.log("teacher_student.js loaded");

//                     student_management.teacher.show_students(frm);

//                 }
//             );

//         });

//     }
// });

