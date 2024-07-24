from odoo import models, fields, api, exceptions, _

class SubstituteProductWizard(models.TransientModel):
    _name = 'substitute.product.wizard'
    _description = 'Substitute Product Wizard'

    sale_order_line_id = fields.Many2one('sale.order.line', string='Original Product', required=True)
    substitute_product_ids = fields.Many2many('product.product', string='Available Substitute Products')
    selected_substitute_product_id = fields.Many2one('product.product', string='Selected Substitute Product')
    order_id = fields.Many2one('sale.order', string='Order')

    @api.onchange('sale_order_line_id')
    def _get_available_substitute_products(self):
        if not self.sale_order_line_id:
            self.substitute_product_ids = [(5, 0, 0)]
            return

        product_template = self.sale_order_line_id.product_id.product_tmpl_id
        if product_template:
            available_substitutes = product_template.substitute_product_ids
            available_substitute_products = self.env['product.product'].search([
                ('product_tmpl_id', 'in', available_substitutes.ids),
                ('qty_available', '>', 0)
            ])
            print("Available substitutes:", available_substitute_products)  # Debug
            if not available_substitute_products:
                raise exceptions.UserError(_('No alternate products available.'))
            self.substitute_product_ids = [(6, 0, available_substitute_products.ids)]
        else:
            self.substitute_product_ids = [(5, 0, 0)]

    def substitute_product(self):
        self.ensure_one()

        if not self.sale_order_line_id:
            raise exceptions.UserError(_('No sale order line found to update.'))

        if not self.selected_substitute_product_id:
            raise exceptions.UserError(_('No substitute product selected.'))

        substitute_product_variant = self.selected_substitute_product_id
        sale_order_line = self.sale_order_line_id
        sale_order = sale_order_line.order_id

        print("Selected substitute product:", substitute_product_variant)  # Debug

        if sale_order_line.is_substituted and sale_order_line.product_id == substitute_product_variant:
            raise exceptions.UserError(_('The selected substitute product is already applied to this line.'))

        sale_order_line.write({
            'product_id': substitute_product_variant.id,
            'name': substitute_product_variant.display_name,
            'price_unit': substitute_product_variant.lst_price,
            'is_substituted': False
        })

        sale_order.write({
            'original_product_id': sale_order_line.product_id.product_tmpl_id.id,
            'substitute_product_id': substitute_product_variant.product_tmpl_id.id
        })

        return {'type': 'ir.actions.act_window_close'}
