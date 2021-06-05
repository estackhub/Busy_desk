# Copyright (c) 2021, Jide Olayinka and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

# delete below just pass
class StatementViewer(Document):
	def populate_recipient_list(self):
	# Get list of customers and email addresses, append to table
		self.recipients = [];
		customer_list = get_recipient_list()
		for c in customer_list:
			row = self.append('recipients', {})
			row.customer = c.customer
			row.contact = c.contact
			row.email = c.email_id
			row.send_statement = c.send_statement
