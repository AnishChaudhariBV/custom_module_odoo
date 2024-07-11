from odoo import models, fields, _,api
from odoo.exceptions import UserError,ValidationError


class SalesOrder(models.Model):
    _inherit = "sale.order"

    check_date = fields.Boolean()
    nick_name = fields.Char()

    # related = 'picking_ids.nick_name'
    def action_confirm(self):
            res = super(SalesOrder, self).action_confirm()
            for order in self:
                for line in order.order_line:
                    if not line.is_available:
                        raise ValidationError("One or more products in the order are not available in sufficient quantity.")

            return res

    def action_cancel(self):
        if self.check_date:
            raise UserError(_('Please Uncheck The CheckBox!!!!!'))

    def action_print_report(self):
        res= self.env['sale.order.line'].browse(self._context.get('active_id'))
        print(res)

        return{
            'type': 'ir.actions.act_window',
            'name': 'print Report',
            'res_model': 'wiz.report',
            'view_mode': 'form',
            'target': 'new',
            'context':{'default_order_id':self.id}

        }



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    custom_name = fields.Char(string="Custom Name")
    is_available = fields.Boolean(string="Is Available", compute="_compute_available_or_not")
    product_image = fields.Binary(string="Product Image", related='product_id.image_1920', depends=['product_id'])

    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({
            'product_image': self.product_image,
        })
        return values

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({
            'product_image': self.product_image
        })
        return res

    @api.depends('product_uom_qty', 'order_id.partner_id')
    def _compute_available_or_not(self):
        for rec in self:
            product = rec.product_id
            if product:
                product_tmpl_id = product.product_tmpl_id
                qty_available = self.env['product.template'].browse(product_tmpl_id.id).qty_available
                rec.is_available = rec.product_uom_qty <= qty_available
            else:
                rec.is_available = False



    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({'custom_name': self.custom_name})
        return values

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_custom_move_fields(self):
        fields = super(StockRule, self)._get_custom_move_fields()
        fields += ['custom_name']
        return fields

class StockMove(models.Model):
    _inherit = 'stock.move'
    custom_name = fields.Char(string="Custom Name")
    product_image = fields.Binary(string="Product Image")



class StockPicking(models.Model):
    _inherit = 'stock.picking'
    nick_name= fields.Char(string="Nick Name")





