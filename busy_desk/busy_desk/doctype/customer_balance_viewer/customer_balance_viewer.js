// Copyright (c) 2021, Jide Olayinka and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Balance Viewer', {
	refresh: function(frm) {
		var today = frappe.datetime.nowdate();
		frm.set_value('from_date', today);
		frm.set_value('to_date', today);

	},
	summary: function (frm) {
		frappe.call({
			method: "busy_desk.api.get_schedule_content",
			args: {
				company: frm.doc.company,
				from_date: frm.doc.from_date,
				to_date: frm.doc.to_date,
				customer_group:frm.doc.customer_group
			  },
			callback: function (r) {
				var x = window.open();
				x.document.open().write(r.message);
			  }
		  });
	  },
	  send_email: function (frm) {
		//if (frm.doc.customer != undefined && frm.doc.customer != "") { //send_individual_statement
		  frappe.call({
			method: "busy_desk.api.send_toeach_director",
			
			callback: function (r) {
			  frappe.msgprint(__("Email queued to be sent to customer"))
			}
		  });
		/* }
		else {
		  frappe.msgprint('Please select a customer');
		} */
	  },	  
});
