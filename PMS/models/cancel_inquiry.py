from odoo import models, fields, api

class InquiryCancellation(models.Model):
    _name = 'property.inquiry.cancellation'
    _description = 'Property Inquiry Cancellation'

    inquiry_id = fields.Many2one('property.inquiry', string='Inquiry')
    reason = fields.Text(string='Reason')

    def save(self):
        print(">>>>>>>>>>>>>")

    @api.model
    def create(self, values):
        inquiry_id = values.get('inquiry_id')
        if inquiry_id:
            inquiry = self.env['property.inquiry'].browse(inquiry_id)
            inquiry.write({'message': 'cancelled '})
            print(type(inquiry))
        return super(InquiryCancellation, self).create(values)

