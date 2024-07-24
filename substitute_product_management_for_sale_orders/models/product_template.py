from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    substitute_product_ids = fields.Many2many(
        'product.template',
        'product_alternative_rel',
        'src_id',
        'dest_id',
        string="Alternative Products"
    )
