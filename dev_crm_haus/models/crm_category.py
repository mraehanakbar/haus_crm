import random
from email.policy import default
from odoo import api, fields, models, _
from datetime import datetime


class CrmCategory(models.Model):
    _name = "crm.category"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "CRM Category Form"

    # Define Some Fields Or Function Here
    name = fields.Char(String="Name", tracking=True)
    category_priority = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ], string="Priority")

    # def generate_random_name(length=5):
    #     vowels = "aeiou"
    #     consonants = "bcdfghjklmnpqrstvwxyz"
    #     name = ""

    #     for i in range(length):
    #         if i % 2 == 0:
    #             name += random.choice(consonants)
    #         else:
    #             name += random.choice(vowels)

    #     return name.capitalize()

    def new_category(self):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        name = ""
        length = 5

        for i in range(length):
            if i % 2 == 0:
                name += random.choice(consonants)
            else:
                name += random.choice(vowels)

        self.env['crm.category'].sudo().create({
            'name': name
        })
