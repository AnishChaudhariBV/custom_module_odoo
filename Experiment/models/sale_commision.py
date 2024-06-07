from odoo import models, fields, api

class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = 'For testing menu purpose'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Salesperson",
        store=True
    )

    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")

    sale_order_ids = fields.One2many(
        'sale.commission.line',
        'commission_id',
        string='Sale Orders',
        compute='calculate_orders',
        store=True
    )
    total_orders = fields.Integer(string='Total Orders', compute='calculate_orders',store=True)
    total_commission_value = fields.Float(string='Total Commission', compute='calculate_orders',store=True)

    @api.depends('user_id', 'start_date', 'end_date')
    def calculate_orders(self):
        for commission in self:
            if commission.user_id and commission.start_date and commission.end_date:
                sale_commission_lines = self.env['sale.commission.line'].search([
                    ('salesperson_id', '=', commission.user_id.id),
                    ('create_date', '>=', commission.start_date),
                    ('create_date', '<=', commission.end_date)
                ])

                total_orders = len(sale_commission_lines)
                total_commission_value = sum(line.total_commission for line in sale_commission_lines)

                commission.update({
                    'sale_order_ids': [(6, 0, sale_commission_lines.ids)],
                    'total_orders': total_orders,
                    'total_commission_value': total_commission_value,
                })
            else:
                commission.update({
                    'sale_order_ids': [(5, 0, 0)],
                    'total_orders': 0,
                    'total_commission_value': 0,
                })


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        sale_commission_line_obj = self.env['sale.commission.line']
        for order in self:
            total_commission = order.amount_total * (order.user_id.percent_commission / 100) if order.user_id.order_value < order.amount_total else 0
            order_data = {
                'number': self.name,
                'customer_id': self.partner_id.id,
                'salesperson_id': self.user_id.id,
                'total_amount': self.amount_total,
                'create_date': self.date_order,
                'order_value': self.user_id.order_value,
                'percentage': self.user_id.percent_commission,
                'total_commission': total_commission
            }
            sale_commission_line_obj.create(order_data)
        return super(SaleOrder, self).action_confirm()

    def action_cancel(self):
        sale_commission_line_obj = self.env['sale.commission.line']
        lines_to_delete = sale_commission_line_obj.search([('number', '=', self.name)])
        lines_to_delete.unlink()
        return super(SaleOrder, self).action_cancel()


class ResPartner(models.Model):
    _inherit = 'res.partner'

    percent_commission = fields.Integer(string='Percentage', default=16)
    order_value = fields.Float(string='Order Value')
    sale_ids = fields.One2many('sale.order', 'partner_id', string='Sales Details')
    total = fields.Float(compute='_compute_total', string='Total Sales')

    @api.depends('sale_ids')
    def _compute_total(self):
        for partner in self:
            total = sum(order.amount_total for order in partner.sale_ids)
            partner.total = round(total, 2)

    def print_mail(self):
        template = self.env.ref('Experiment.email_customer_template')
        ctx = {
            'default_model': 'res.partner',
            'default_res_id': self.id,
            'default_template_id': template.id if template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_light',
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }


class SaleCommissionLine(models.Model):
    _name = 'sale.commission.line'
    _description = 'Sale Commission Line'

    number = fields.Char(string='Number')
    customer_id = fields.Many2one('res.partner', string='Customer')
    salesperson_id = fields.Many2one('res.users', string='Salesperson', readonly=True)
    total_amount = fields.Float(string='Total Amount')
    create_date = fields.Datetime(string="Creation Date", index=True, readonly=True)
    order_value = fields.Integer(string='Order Value Above Commission', readonly=True)
    percentage = fields.Float(string='Percentage', readonly=True)
    total_commission = fields.Float(string="Commission Value")
    commission_id = fields.Many2one('sale.commission', string='Commission Reference')
