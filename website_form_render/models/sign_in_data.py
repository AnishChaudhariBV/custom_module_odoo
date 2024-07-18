from odoo import models, fields


class SignInUserData(models.Model):
    _name = 'signin.user.data'
    _description = 'signin.user.data'

    name = fields.Char(string='Name', required=True)
    mobile = fields.Char(string='Mobile Number', required=True)
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address', required=True)