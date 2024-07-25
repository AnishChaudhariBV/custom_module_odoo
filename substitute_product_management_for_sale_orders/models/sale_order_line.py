from odoo import models, fields, api, exceptions, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_substituted = fields.Boolean(string='Is Substituted', readonly=False)

    @api.onchange('product_id')
    def _check_product_availability(self):
        if self.product_id:
            product_qty_available = self.product_id.qty_available
            if self.product_uom_qty > product_qty_available:
                self.is_substituted = True
            else:
                self.is_substituted = False


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_substituted_lines = fields.Boolean(
        string='Has Substituted Lines',
        compute='_compute_has_substituted_lines',
        store=True
    )
    original_product_id = fields.Many2one('product.template', string='Original Product')
    substitute_product_id = fields.Many2one('product.template', string='Substituted Product')

    @api.depends('order_line.is_substituted')
    def _compute_has_substituted_lines(self):
        for order in self:
            order.has_substituted_lines = any(line.is_substituted for line in order.order_line)

    def action_substitute_product_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Substitute Products',
            'res_model': 'substitute.product.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id}
        }

    def action_confirm(self):
        if self.has_substituted_lines:
            raise exceptions.UserError(
                _('Please add substitute products because the product is not available.')
            )
        return super(SaleOrder, self).action_confirm()
