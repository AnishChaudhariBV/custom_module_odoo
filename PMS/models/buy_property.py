from odoo import models, fields, api, _

class PropertyPurchase(models.Model):
    _name = 'property.purchase'
    _description = 'Property Purchase'

    name = fields.Many2one('property.inquiry', string='Buyer', required=True)
    property_id = fields.Many2one('property.list', string='Property', required=True)
    property_price = fields.Float(string='Property', required=True)
    purchase_price = fields.Float(string='Purchase Price', required=True)
    purchase_date = fields.Date(string='Purchase Date', default=fields.Date.today)
    sequence_no = fields.Char(string='Sequence No:', readonly=True, copy=False, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sequence_no', _('New')) == _('New'):
            vals['sequence_no'] = self.env['ir.sequence'].next_by_code('buyer.sequence') or _('New')
        return super(PropertyPurchase, self).create(vals)

    def confirm(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Property Bought Successfully',
                'type': 'rainbow_man',
            }
        }

    @api.onchange('property_id')
    def _onchange_property_id(self):
        if self.property_id:
            self.property_price = self.property_id.price
