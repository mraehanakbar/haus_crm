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
    question_user = fields.Char(related='questionare_id.email_employee')
    question_audit_fields = fields.Char(string="Question")
    answer_audit_fields = fields.Text(string="Answer")
    questions_type_fields = fields.Selection([
        ('pilihan_ganda','Pilihan Ganda'),
        ('text','Text'),
        ('true_false','Benar Atau Salah')
        ],string="Tipe Pertanyaaan")
    questions_yes_no_choice_fields = fields.Selection([
        ('yes','Ya'),
        ('no','Tidak'),
        ],string="Pilihan")
    questions_selection_choice = fields.Many2one('crm.selections.answers',string="Answers", domain = "[('questions_name','=',question_audit_fields)]")
    question_answered_fields =  fields.Boolean(string='Have Been Answered',compute='function_type_confirmation_fields')

    @api.depends('question_answered_fields')
    def function_type_confirmation_fields(self):
        if self.questions_type_fields == 'pilihan_ganda':
            if self.questions_selection_choice:
                self.question_answered_fields = True
            else:
                self.question_answered_fields = False
        if self.questions_type_fields == 'text':
            if self.answer_audit_fields:
                self.question_answered_fields = True
            else:
                self.question_answered_fields = False
        if self.questions_type_fields == 'true_false':
            if self.questions_yes_no_choice_fields:
                self.question_answered_fields = True
            else:
                self.question_answered_fields = False