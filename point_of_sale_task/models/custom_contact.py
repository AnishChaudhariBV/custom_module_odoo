from odoo import fields, models


class PosConfigCustomer(models.Model):
    _name = 'custom.contact'
    _rec_name='name'

    name=fields.Char(string="Name")
    mo_no=fields.Text(string="MobileNO:")

