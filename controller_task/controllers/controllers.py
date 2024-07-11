from odoo import http
from odoo.http import request, Response
from werkzeug.exceptions import Forbidden

class CustomController(http.Controller):

    @http.route('/custom_controller', type='json', auth="public", methods=['POST'])
    def custom_controller(self, **kwargs):
        req = request.get_json_data()

        partner_id = req.get('partner_id')
        order_lines = req.get('order_lines', [])

        partner = request.env['res.partner'].sudo().browse(partner_id)
        if not partner.exists():
            return Forbidden("Partner ID does not exist.")

        if not order_lines:
            return Forbidden("Order lines are required.")

        order_vals = {
            'partner_id': partner_id,
            'order_line': [(0, 0, {
                'product_id': order.get('product_id'),
                'product_uom_qty': order.get('quantity'),
                'price_unit': order.get('price'),
            }) for order in order_lines]
        }

        sale_order = request.env['sale.order'].sudo().create(order_vals)

        return {
            "message": "Order Create Successfully",
            "order_id": sale_order.id
        }
