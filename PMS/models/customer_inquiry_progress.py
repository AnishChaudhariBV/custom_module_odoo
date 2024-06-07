from odoo import models, fields, api

class Progress(models.Model):
    _name = 'progress.status'
    _description = 'Progress Property'

    name = fields.Many2one('property.inquiry', string='Name')
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Status', default='draft')
    percent_complete = fields.Float(string='Percentage Complete', default=0)

    def save(self):
        print(">>>>>>>>>>>>>>>>")

    @api.model
    def create(self, values):
        inquiry_id = values.get('name')
        if inquiry_id:
            inquiry = self.env['property.inquiry'].browse(inquiry_id)
            inquiry.write({'message': values.get('description', '')})
        return super(Progress, self).create(values)
