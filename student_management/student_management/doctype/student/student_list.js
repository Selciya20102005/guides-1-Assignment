console.log("STUDENT LIST JS FILE LOADED");

frappe.listview_settings['Student'] = {

    add_fields: ['status2'],

    get_indicator(doc) {

        console.log("GET INDICATOR:", doc.name, doc.status2);

        if (doc.status2 === 'Active') {
            return [
                __('Active'),
                'green',
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

    }

};