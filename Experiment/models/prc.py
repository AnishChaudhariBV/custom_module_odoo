from odoo import models, fields, _,api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "account.move.line"

    product_image = fields.Binary(string="Product Image", related='product_id.image_1920', depends=['product_id'])



# class ResPartner(models.Model):
#     _inherit = "res.partner"
#
#     def schedule_meeting(self):
#         # view_info = self.env['ir.ui.view'].search([('model', '=', 'res.partner'), ('type', '=', 'form')])
#         # print(view_info)
#
#         # partners = self.env['res.partner'].search([('phone', '=', '+91')])
#         # print(partners)
#         # pd= self.env['res.partner'].browse(10)
#         # print(pd)
#         # for i in partners:
#         #     if i.id<=20:
#         #         display_name = i.display_name
#         #         print(display_name)
#
#         # partner_fields = self.env['res.partner'].fields_get()
#         # for field_name, field_definition in partner_fields.items():
#         #     print(f"Field Name: {field_name}")
#         #     print(len(field_name))
#         # # a=self.env['res.partner'].search([])
#         # for i in a:
#         #     if i.id % 2 ==0:
#         #        i.write({'phone':'+91'})
#         #     print('Update Phone number is sucessfully')
#
#         return True


# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     order_line_ids = fields.One2many('sale.order.line', 'order_id', string='Order Lines')
#
# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     product_id = fields.Many2one('product.product', string='Product', required=True)
#
#     @api.constrains('product_id', 'order_id')
#     def _check_unique_product_per_order(self):
#         for line in self:
#             if line.order_id and line.order_id.order_line_ids.filtered(lambda x: x.product_id == line.product_id and x != line):
#                 raise ValidationError(f"The product {line.product_id.name} is already selected in this order.and you want to the more quantity so add the products quantity")