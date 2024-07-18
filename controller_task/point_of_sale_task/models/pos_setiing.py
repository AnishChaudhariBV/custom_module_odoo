from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_value = fields.Float(string="Discount Value", default=50.00, config_parameter='web_pos.discount_value')
