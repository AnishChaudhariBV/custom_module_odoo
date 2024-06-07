from odoo import fields, models, api
from datetime import timedelta

class PrintReport(models.TransientModel):
    _name = 'wiz.report'    
    order_lines = fields.Many2many(
        comodel_name='sale.order.line',
        string="Order Lines",
     )
    order_id=fields.Many2one('sale.order', 'order_id')
    partner_id = fields.Many2one(comodel_name='res.partner', related="order_id.partner_id",string="Customer", readonly=True)
    company_id = fields.Many2one(comodel_name='res.company', related="order_id.company_id",readonly=True)
    partner_shipping_id = fields.Many2one(
        comodel_name='res.partner',
        string="Delivery Address",
        compute='_compute_partner_shipping_id',
        store=True, readonly=False, required=True, precompute=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", )

    state = fields.Selection(related='order_id.state')
    date_order = fields.Datetime(related='order_id.date_order')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        compute='_compute_user_id',
        store=True, readonly=False, precompute=True, index=True,
        tracking=2,
        domain=lambda self: "[('groups_id', '=', {}), ('share', '=', False), ('company_ids', '=', company_id)]".format(
            self.env.ref("sales_team.group_sale_salesman").id
        ))
    validity_date = fields.Date(
        string="Expiration",
        compute='_compute_validity_date',
        store=True, readonly=False, copy=False, precompute=True)

    @api.depends('company_id')
    def _compute_validity_date(self):
        today = fields.Date.context_today(self)
        for order in self:
            days = order.company_id.quotation_validity_days
            if days > 0:
                order.validity_date = today + timedelta(days)
            else:
                order.validity_date = False
    @api.depends('partner_id')
    def _compute_user_id(self):
        for order in self:
            if order.partner_id and not (order._origin.id and order.user_id):
                # Recompute the salesman on partner change
                #   * if partner is set (is required anyway, so it will be set sooner or later)
                #   * if the order is not saved or has no salesman already
                order.user_id = (
                        order.partner_id.user_id
                        or order.partner_id.commercial_partner_id.user_id
                        or (self.user_has_groups('sales_team.group_sale_salesman') and self.env.user)
                )
    @api.depends('partner_id')
    def _compute_partner_shipping_id(self):
        for order in self:
            order.partner_shipping_id = order.partner_id.address_get(['delivery'])[
                'delivery'] if order.partner_id else False

    def Print(self):
        
         return  self.print_customize_qweb_report()

    def print_customize_qweb_report(self):
        if not self.order_lines:
            # If no order lines are selected, automatically select all order lines
            self.order_lines = self.env['sale.order.line'].search([('order_id', '=', self.order_id.id)])
        return self.env.ref('Experiment.action_Qwebwiz_report_id').report_action(self)


  








