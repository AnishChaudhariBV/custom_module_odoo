from odoo import fields, models


class PosConfigLocation(models.Model):
    _inherit = 'pos.config'

    location_ids = fields.Many2many('res.location', string="Enable Location")
    location_enable = fields.Boolean(String="Location")
    contact_ids=fields.Many2many('custom.contact', string="Enable Contact")
