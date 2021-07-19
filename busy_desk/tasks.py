import frappe
from busy_desk.api import send_balances


def all():
    #no code here
    pass


def cronstom():
    # Sunday not included

    # call send mail from api        
    send_balances()
    
    
    