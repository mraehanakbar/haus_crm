from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime

class CrmCategory(models.Model):
    _name = "crm.category"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Category Form"
    _rec_name = "name"
    
    #Define Some Fields Or Function Here
    name = fields.Char(String="Name", tracking=True)
    category_priority = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ], string="Priority")
