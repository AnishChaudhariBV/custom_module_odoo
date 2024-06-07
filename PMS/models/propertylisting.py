from odoo import models, fields , api,_
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property.list'
    _description = 'Property Management'
    _inherit = ['mail.thread','mail.activity.mixin']


    property_type = fields.Selection([('residential', 'Residential'),
                                      ('commercial', 'Commercial'),
                                      ('industrial', 'Industrial')],
                                     string='Property Type')
    name = fields.Char(string='Property Name/Title')
    address = fields.Char(string='Address')
    description = fields.Char(string='Description')
    price = fields.Float(string='Price/Rent')
    property_size = fields.Float(string='Property Size/Area')
    bedrooms = fields.Integer(string='Number of Bedrooms')
    bathrooms = fields.Integer(string='Number of Bathrooms')
    floor_plan = fields.Binary(string='Floor Plan')
    images = fields.Binary(string='Images')
    features = fields.Html(string='Features/Amenities')
    availability_status = fields.Selection([('available', 'Available'),
                                            ('under_contract', 'Under Contract'),
                                            ('rented', 'Rented')],
                                           string='Availability Status')
    contact_name = fields.Char(string='Contact Name', required=True)
    contact_phone = fields.Char(string='Contact Phone', required=True)
    contact_email = fields.Char(string='Contact Email')
    additional_details = fields.Text(string='Additional Details')
    date_listed = fields.Date(string='Date Listed', default=fields.Date.today)
    property_id = fields.Char(string='Property ID/Reference Number', required=True)

    listed_property_count = fields.Integer(string='Listed Property Count', compute='_compute_listed_property_count')

    @api.model
    def default_get(self,fields):
        res=super(Property,self).default_get(fields)
        print(res)
        return res

    @api.depends('property_type')
    def _compute_listed_property_count(self):
        for record in self:
            listed_property_count = self.env['property.list'].search_count([('property_type', '=', record.property_type)])
            record.listed_property_count = listed_property_count

    def save(self):
        print("..............")


    @api.constrains('additional_details')
    def _compute_additional_details(self):
        for record in self:
            if not record.additional_details:
                record.additional_details = record.description

    @api.constrains('property_id')
    def _check_unique_property_id(self):
        for record in self:
            if record.property_id:
                existing_property = self.search([('property_id', '=', record.property_id)])
                if existing_property.exists() and len(existing_property) > 1:
                    raise ValidationError("Property ID/Reference Number must be unique!")

    def action_property_list(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Property Listing',
            'res_model': 'property.list',
            'view_mode': 'kanban,tree,form',
            'target': 'new',
            'domain': [('property_type', '=', self.property_type)]
        }

    def Check_wiz(self):
        # properties_id = self.env['property.list'].search([])
        # properties = self.env['property.list'].browse([properties_id]).write({'name':'Flat'})
        # properties_id = self.env['property.list'].create({'contact_name':'Anish','contact_phone':'9265860069','property_id':'#2565412'})
        # property = self.env['property.list'].search([('property_id', '=', 'fcgfg')])
        # if property:
        #  property.unlink()

         return {'type': 'ir.actions.act_window',
            'res_model': 'update.price',
            'view_mode': 'form',
            'target': 'new'}
