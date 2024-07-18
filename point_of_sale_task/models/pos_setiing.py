from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_value = fields.Float(string="Discount Value", default=50.00, config_parameter='point_of_sale_task.discount_value')
