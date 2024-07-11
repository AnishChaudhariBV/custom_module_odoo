from odoo import models, fields, _,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # pos.config fields
    sales_limit = fields.Float(string='Sales Limit', readonly=False, config_parameter='practice.sales_limit')

class SalesOrder(models.Model):
    _inherit = "sale.order"
    state=fields.Selection(selection_add=[("approve",'Approve')])

    def action_confirm(self):
        for order in self:
            conf=float(self.env['ir.config_parameter'].sudo().get_param('experiment.sales_limit'))
            if conf<order.amount_total:
                order.state='approve'
            else:
                 super(SalesOrder, self).action_confirm()

    def _can_be_confirmed(self):
        self.ensure_one()
        return self.state in {'draft', 'sent', 'approve'}

    def approve_sale(self):
        super(SalesOrder, self).action_confirm()



