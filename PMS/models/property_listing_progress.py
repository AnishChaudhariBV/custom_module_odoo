from odoo import models, fields, api

class Progress(models.Model):
    _name = 'list.progress'
    _description = 'Property Progress'

    property_id = fields.Many2one('property.list', string='Property')
    progress_date = fields.Date(string='Progress Date')
    progress_description = fields.Text(string='Progress Description')
    progress_stage = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Progress Stage')

    sequence = fields.Integer(string='seq.')

    def save(self):
        print(">>>>>>>>>>>>>>>>>.>>>>>>>>>>>>>>>")


    @api.model
    def create(self, values):
        property_id = values.get('property_id')
        if property_id:
            property_record = self.env['property.list'].browse(property_id)
            property_record.write({'Progress': values.get('progress_description', '')})
        return super(Progress, self).create(values)
