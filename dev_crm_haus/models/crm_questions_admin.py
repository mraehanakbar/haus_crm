from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime
from odoo.exceptions import ValidationError

class CrmQuestionsAdmin(models.Model):
    _name = "crm.questions.admin"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Questions Admin"
    _rec_name = "questionare_id"

    @api.model
    def create(self,vals):
        vals['status'] = 'submitted'
        try:
            if vals['questions_type_fields'] == 'pilihan_ganda':
                if len(vals['questions_selection_choice']) < 2:
                    raise ValidationError("Minimal Harus ada 2 Pilihan Jawaban Periksa Kembali list jawaban anda")
        except:
            raise ValidationError("Harus ada 2 atau lebih pilihan Jawaban")
        rec = super(CrmQuestionsAdmin, self).create(vals)
        return rec
    
    questionare_id = fields.Many2one('crm.questionare.admin')
    questionare_name = fields.Char(related='questionare_id.questionare_name_fields')
    question_audit_fields = fields.Char(string="Question",required = True)
    questions_type_fields = fields.Selection([
        ('pilihan_ganda','Pilihan Ganda'),
        ('text','Text'),
        ('true_false','Benar Atau Salah')
        ],string="Type" ,required = True)
    questions_yes_no_choice_fields = fields.Selection([
        ('n_a','N/A'),
        ('yes','Ya'),
        ('no','Tidak'),
        ],string="Pilihan",required=True)
    questions_selection_choice = fields.One2many('crm.selections.answers','questions_id',string="Answers" )
    status = fields.Selection([('drafted','Drafted'),
    ('submitted','Submitted')
    ],string='status',default='drafted')

class CrmSelectionsAnswers(models.Model):
    _name = "crm.selections.answers"
    _description = "Selections Admin"
    _rec_name = "answers_selections"

    questions_id = fields.Many2one('crm.questions.admin')
    questions_name =  fields.Char(related="questions_id.question_audit_fields")
    answers_selections = fields.Char(string='Answers')