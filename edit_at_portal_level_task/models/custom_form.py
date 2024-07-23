from odoo import models, fields

class CustomForm(models.Model):
    _name = 'custom.form'
    _description = 'My custom Form Model'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    message = fields.Text(string='Message')
