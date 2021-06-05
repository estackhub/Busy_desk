// Copyright (c) 2021, Jide Olayinka and contributors
// For license information, please see license.txt

frappe.ui.form.on('Statement Viewer', {
	refresh: function (frm) {
		// Default values in From and To Dates
		var today = frappe.datetime.nowdate();
		frm.set_value('from_date', frappe.datetime.month_start(today));
		frm.set_value('to_date', today);
	  },
	  
	  preview: function (frm) {
		if (frm.doc.customer != undefined && frm.doc.customer != "") {
		  frappe.call({
			method: "busy_desk.api.get_report_content",
			args: {
			  company: frm.doc.company,
			  customer_name: frm.doc.customer,
			  from_date: frm.doc.from_date,
			  to_date: frm.doc.to_date
			},
			callback: function (r) {
			  var x = window.open();
			  x.document.open().write(r.message);
			}
		  });
		}
		else {
		  frappe.msgprint('Please select a customer');
		}
	  },
	  letter_head: function (frm) {
		cur_frm.save();
	  },
	  no_ageing: function (frm) {
		cur_frm.save();
	  },
	
	});
	
