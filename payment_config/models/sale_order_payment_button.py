from odoo import models, _, fields
from odoo.exceptions import UserError
import json

class SalesOrder(models.Model):
    _inherit = "sale.order"

    def action_payment_with_cybersource(self):
        self.ensure_one()

        provider = self.env['payment.provider'].search([('code', '=', 'cybersource')], limit=1)
        print(provider)
        if not provider:
            raise UserError(_("CyberSource payment provider is not configured."))

        try:
            response = provider.process_payment_with_cybersource(
                amount=self.amount_total,
                currency=self.currency_id.name,
                order_id=self.name
            )

            print("CyberSource Response:", response)

            status = response.get('status', 'UNKNOWN')
            message = response.get('message', 'No message')

            if status == 'AUTHORIZED':
                self.env['payment.transaction'].create({
                    'amount': self.amount_total,
                    'currency_id': self.currency_id.id,
                    'provider_id': provider.id,
                    'reference': self.name,
                    'partner_id': self.partner_id.id,
                    'state': 'done',
                    'create_date': fields.Datetime.now(),
                    'payment_method_id': provider.id,
                })

                # Update sale order state to 'sale' to confirm the order
                self.write({'state': 'sale'})
                print("Payment successfully processed and transaction record created. Order state updated to 'sale'.")
            else:
                raise UserError(_("Payment failed: " + message if message != 'No message' else 'Payment failed: No additional details provided'))
        except Exception as e:
            raise UserError(_(f"Payment processing error: {str(e)}"))


     
     
     
     
     
     
     
     