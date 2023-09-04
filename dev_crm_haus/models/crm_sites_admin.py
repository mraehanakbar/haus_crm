from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
import csv
import base64
from pytz import timezone 
from lxml import etree

class CrmSitesAdmin(models.Model):
    _name = "crm.sites.admin"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "CRM Sites admin"


    site_name_fields = fields.Char(string='Site Name')
    site_address_fields = fields.Char(string='Site Address Fields')
    country_sites_fields = fields.Char(string='Country Fields')
    province_sites_fields = fields.Char(string='Province Fields')
    city_sites_fields = fields.Char(string='City Fields')