from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmQuestionsAdmin(models.Model):
    _name = "crm.questions.admin"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Questions Admin"
    _rec_name = "questionare_id"

    questionare_id = fields.Many2one('crm.questionare.admin')
    questionare_name = fields.Char(related='questionare_id.questionare_name_fields')
    question_audit_fields = fields.Char(string="Question")