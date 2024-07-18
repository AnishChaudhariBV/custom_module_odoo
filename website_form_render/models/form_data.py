from odoo import models, fields

class CustomFormData(models.Model):
    _name = 'custom.form.data'
    _description = 'Custom Form Data'

    name = fields.Char(string='Name', required=True)
    mobile = fields.Char(string='Mobile Number', required=True)
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address', required=True)







