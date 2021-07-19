from busy_desk.api import send_balances
import frappe
from frappe.utils import (
    today,
    format_time,
    global_date_format,
    now,
    get_first_day,
)

def all():
    
    pass


def cronstom():
    # Sunday not included

    # call send mail from api        
    send_balances()
    
    date_time = global_date_format(now()) + " " + format_time(now())
    new_note = frappe.get_doc({"doctype": "Note",
        "title": "Always Sent" + date_time
    })
    new_note.insert()
    frappe.db.commit()
    