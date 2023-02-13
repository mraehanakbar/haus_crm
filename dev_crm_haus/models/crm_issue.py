from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmIssue(models.Model):
    _name = "crm.issue"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CRM Issue Form"

    # Define Some Fields Or Function Here
    issue_problem = fields.Char(String="Problem", required=True)
    issue_category = fields.Many2one(
        "crm.category", String="Category", required=True)
    issue_due_date = fields.Datetime(String="Due Date")
    issue_comment = fields.Text(String="Comment")
    issue_attachment = fields.Binary("Attachment", attachment=True)
