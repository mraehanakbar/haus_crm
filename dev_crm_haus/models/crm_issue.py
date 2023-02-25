from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime

department_list = [
        ('OPERATION','Operation'),
        ('HUMAN RESOURCES','Human Resources'),
        ('PROCUREMENT & SUPPLY CHAIN','Procurement & Supply Chain'),
        ('FINANCE & ACCOUNTING','Finance & Accounting'),
        ('MARKETING','Marketing'),
        ('INTERNAL AUDIT','Internal Audit'),
        ('GENERAL MANAGEMENT','General Management'),
        ('BUSINESS DEVELOPMENT','Bussiness Development'),
        ('TECHNOLOGY','Technology'),
    ]
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
    
    employee_id = fields.Many2one(
    "employee.data", String="Employee", required=True)
    department = fields.Selection(String="Departemen", related='employee_id.organization_employee')

    issue_department = fields.Selection(department_list)


# Random function
    # @api.multi
    # def get_dep_rec(self):
    #     sql = "SELECT DISTINCT organization_employee FROM employee.data"
    #     self.env.cr.execute(sql)
    #     temp = self.env.cr
    #     for rec in self.env.cr.fetchall():
    #         return {'domain': {'employee_id.organization_employee'}}
#    _defaults = {
#       'status_by': lambda self, cr, uid, context:
#   self.pool.get('res.users').browse(cr, uid, uid, context=context).name,
#    }
#    @api.depends('employee_id')
#    def _get_current_user(self):
#        for rec in self:
#           rec.employee_id = self.env.user.employee_id.id
