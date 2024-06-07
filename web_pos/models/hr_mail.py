from odoo import models, api


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    @api.model
    def action_send_email(self, record_ids):
        records = self.browse(record_ids)
        for record in records:
            template_id = self.env.ref('web_pos.email_template_id').id
            self.env['mail.template'].browse(template_id).send_mail(record.id, force_send=True)
