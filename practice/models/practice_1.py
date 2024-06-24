from odoo import fields, models, api
from datetime import date, datetime


class PracticePrc(models.Model):
    _name = 'practice.prc'
    _description = "practice"
    _rec_name = 'customer_id'

    customer_id = fields.Many2one('res.partner', 'Customer')
    title = fields.Many2one(related='customer_id.title')
    dob = fields.Date('DOB')
    age = fields.Integer('Age', compute='compute_age')
    mobile_no = fields.Integer("Mobile Number")

    @api.depends('dob')
    def compute_age(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0

