from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime

class CrmIssue(models.Model):
    _name = "crm.issue"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Issue Form"

    #Define Some Fields Or Function Here
    