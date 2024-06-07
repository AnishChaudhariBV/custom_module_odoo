from odoo import fields, models, api

class UpdatePrice(models.TransientModel):
    _name = 'update.price'

    property_id = fields.Many2one('property.list', string='Properties to Update')
    new_price = fields.Float(string='New Price')
    price=fields.Float(related='property_id.price', readonly=True)
    diff=fields.Float(compute="_compute_change" , readonly=True)

    @api.depends('price','new_price')
    def _compute_change(self):
        for res in self:
            res.diff = res.new_price-res.price

    def update_price(self):
        self.property_id.write({'price': self.new_price})
        return True
