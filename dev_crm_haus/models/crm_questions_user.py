from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmQuestionsUser(models.Model):
    _name = "crm.questions.user"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Questions User"
    _rec_name = "questionare_id"

    questionare_id = fields.Many2one('crm.questionare.user')
    questionare_name = fields.Char(related='questionare_id.questionare_name_fields')
    question_audit_fields = fields.Char(string="Question")
    answer_audit_fields = fields.Text(string="Answer")