from odoo import fields, models


class PosConfigLocation(models.Model):
    _name = 'res.location'
    _rec_name='location_area'

    location_area = fields.Char(string="locations")
