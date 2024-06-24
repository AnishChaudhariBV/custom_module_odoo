from odoo import fields, models, api
from datetime import date, datetime


class Practice(models.Model):
    _name = 'practice.practice'
    _description = "practice"
    _rec_name = 'title'

    customer_id = fields.Many2one('res.partner', 'Customer')
    title = fields.Many2one(related='customer_id.title')
    dob = fields.Date('DOB')
    age = fields.Integer('Age', compute='compute_age')
    mobile_no=fields.Integer("Mobile Number")


    @api.depends('dob')
    def compute_age(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0
    @api.onchange('mobile_no')
    def _onchange_mobile_no(self):
        if self.customer_id:
            related_records = self.env['practice.prc'].search([('customer_id', '=', self.customer_id.id)])
            print(related_records)
            for record in related_records:
                record.mobile_no = self.mobile_no

    @api.model
    def create(self, vals):
        record = super(Practice, self).create(vals)
        self.env['practice.prc'].create({
            'customer_id': record.customer_id.id,
            'title': record.title.id,
            'dob': record.dob,
            'age': record.age,
            'mobile_no': record.mobile_no
        })
        return record






