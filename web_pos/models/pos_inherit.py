from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = 'pos.order'

    add_note = fields.Char(string='Add Note')
    location = fields.Char(string='location')
    discount_applied=fields.Boolean(string='Discount Applied')

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosOrder, self)._order_fields(ui_order)
        order_fields['add_note'] = ui_order.get('add_note')
        order_fields['discount_applied'] = ui_order.get('discount_applied')
        order_fields['location'] = ui_order.get('location')
        return order_fields

