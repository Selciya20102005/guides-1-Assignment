// window.TeacherStudents = {
//     show_students: function(frm) {
//         frappe.call({
//             method: "frappe.client.get_list",
//             // This is a standard Frappe API method for retrieving a list of documents.
//             args: {
//                 doctype: "Student",
//                 filters: {
//                     teacher: frm.doc.name
//                 },
//                 fields: ["name", "student_name"]
//             },
//             callback: function(r) {
//                 if (!r.message || !r.message.length) {
//                     frappe.msgprint("No students found for this teacher.");
//                     return;
//                 }

//                 let html = "<h4>Students</h4><ul>";

//                 r.message.forEach(student => {
//                     html += `
//                         <li>
//                             ${student.student_name}
//                             (${student.name})
//                         </li>
//                     `;
//                 });

//                 html += "</ul>";

//                 frappe.msgprint({
//                     title: "Teacher's Students",
//                     message: html
//                 });
//             }
//         });
//     }
// };

frappe.provide("student_management.teacher");

student_management.teacher.show_students = function(frm) {

    frappe.call({
        method: "frappe.client.get_list",

        args: {
            doctype: "Student",

            filters: {
                teacher: frm.doc.name
            },

            fields: ["name", "student_name"]
        },

        callback: function(r) {

            if (!r.message || !r.message.length) {
                frappe.msgprint("No students found for this teacher.");
                return;
            }

            let html = "<h4>Students</h4><ul>";

            r.message.forEach(student => {

                html += `
                    <li>
                        ${student.student_name}
                        (${student.name})
                    </li>
                `;

            });

            html += "</ul>";

            frappe.msgprint({
                title: "Teacher's Students",
                message: html
            });
        }
    });
};