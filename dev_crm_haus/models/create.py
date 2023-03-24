from odoo import models, fields, api


class CrmIssueInhert(models.Model):
    _inherit = 'crm.issue'

    @api.model
    def create(self, vals):
        res = super(CrmIssueInhert, self).create(vals)
        res.notif_email()
        return res

    # send email
    def notif_email(self):
        attachment = self.env['ir.attachment'].create({
            'name': 'attachment.pdf',
            'datas': self.issue_attachment,
            'type': 'binary'})
        template_data = {
            'subject': 'Haus Issue Letter',
            'body_html': f'<h1>Dear {self.employee_name}</h1> <h2> kamu mendapatkan masalah/issue berupa {self.issue_problem} dari {self.reporter_name} di cabang {self.temporary_location_selection} </h2>  <p> pada tanggal <b>{self.created_at}</b> dengan kategori {self.issue_category.name} dan prioritas {self.priority} dengan deadline <b>{self.issue_due_date}</b> dengan catatan {self.issue_comment} </p> <p> <img src="data:image/png;base64,${self.issue_attachment}" style="width: 250px;height: 160px;" /> </p>',
            'email_from': 'hrdummyhaus1@gmail.com',
            'auto_delete': True,
            # ini emailnya belum bisa sesuai ke yang ngirim
            'email_to': 'jokopranowow99@gmail.com',

        }
        mail_id = self.env['mail.mail'].sudo().create(template_data)
        mail_id.sudo().send()
