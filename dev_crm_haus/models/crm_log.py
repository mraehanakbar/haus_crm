from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmLog(models.Model):
    _name = "crm.log"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CRM Log Form"

    id_questioner = fields.Many2one('crm.questionare.admin')
    name = fields.Char(String="Name", tracking=True)
    email = fields.Char(String="Email", tracking=True)
    log_date = fields.Date(string="Log Date", default=datetime.today())
    location = fields.Char(string="Location")
    questioner = fields.Char(string="Questioner")
    answer_fields = fields.One2many('crm.questionare.user','questionare_log',compute='_compute_answer_fields')

    @api.depends('questioner')
    def _compute_answer_fields(self):
        for record in self:
            record.answer_fields = self.env['crm.questionare.user'].search([('questionare_name_fields', '=', record.questioner),('email_employee', '=', record.email)])
