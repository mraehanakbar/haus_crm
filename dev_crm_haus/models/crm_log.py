from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmLog(models.Model):
    _name = "crm.log"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CRM Log Form"

    name = fields.Char(String="Name", tracking=True)
    log_date = fields.Date(string="Log Date", default=datetime.today())
    location = fields.Char(string="Location")
