// console.log("TEACHER JS LOADED");
// frappe.ui.form.on("Teacher", {
//     refresh(frm) {
//         frm.add_custom_button("Create Task", () => {
//             let dialog = new frappe.ui.Dialog({
//                 title: "Create Task",

//                 fields: [
//                     {
//                         label: "Task Subject",
//                         fieldname: "task_subject",
//                         fieldtype: "Data",
//                         reqd: 1
//                     }
//                 ],

//                 primary_action_label: "Create Task",

//                 primary_action(values) {
//                     frappe.call({
//                         method: "student_management.task_api.create_task",
//                         args: {
//                             task_subject: values.task_subject
//                         },
//                         callback(response) {
//                             dialog.hide();

//                             frappe.msgprint({
//                                 title: "Success",
//                                 message: `Task ${response.message} created successfully.`,
//                                 indicator: "green"
//                             });
//                         }
//                     });
//                 }
//             });

//             dialog.show();
//         });
//     }
// });