from odoo import models, fields, api, _


class Inquiry(models.Model):
    _name = 'property.inquiry'
    _description = 'property inquiry'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    property_id = fields.Many2one('property.list', string='Property')
    message = fields.Text(string='Message')
    sequence_no = fields.Char(string='Inquiry no.', readonly=True, copy=False, default=lambda self: _('New'))
    active = fields.Boolean(string='Active', default=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', required=True)





    @api.model
    def create(self, vals):
        if vals.get('sequence_no', _('New')) == _('New'):
            vals['sequence_no'] = self.env['ir.sequence'].next_by_code('inquiry.sequence') or _('New')
        return super(Inquiry, self).create(vals)

    def save(self):
        print(">>>>>>>>>>>>>>")
