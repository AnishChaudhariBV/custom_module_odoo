from odoo import models, fields, _
import hashlib
import hmac
import requests
import json
import base64
from datetime import datetime
from odoo.tools.safe_eval import pytz
from odoo.exceptions import UserError

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('cybersource', "Cybersource")],
        ondelete={'cybersource': lambda recs: recs.write({'code': 'other_code'})}
    )
    cybersource_merchant_id = fields.Char(
        string="Merchant ID",
        help="The Merchant ID used to identify the account with Cybersource",
        required_if_provider='cybersource',
    )
    cybersource_api_key_id = fields.Char(
        string="API Key ID",
        help="The API Key ID for the Cybersource account",
        required_if_provider='cybersource',
    )
    cybersource_secret_key = fields.Char(
        string="Secret Key",
        help="The secret key for the Cybersource account",
        required_if_provider='cybersource',
    )

    def _get_gmt_date(self):
        """Get the current date and time in GMT."""
        utc_now = datetime.now(pytz.UTC)
        return utc_now.strftime('%a, %d %b %Y %H:%M:%S GMT')

    def _get_digest(self, payload_bytes):
        """Compute the SHA-256 hash of the payload and return the digest."""
        hashobj = hashlib.sha256()
        hashobj.update(payload_bytes)
        hash_data = hashobj.digest()
        digest = base64.b64encode(hash_data).decode('utf-8')
        return f'SHA-256={digest}'

    def _get_signature(self, method, time, digest):
        """Generate the signature for the request."""
        signature_list = [
            f"host: apitest.cybersource.com",
            f"v-c-date: {time}",
            f"(request-target): {method.lower()} /pts/v2/payments",
            f"digest: {digest}",
            f"v-c-merchant-id: {self.cybersource_merchant_id}"
        ]

        sig_value = '\n'.join(signature_list)
        sig_value_utf = sig_value.encode('utf-8')

        # Decode the secret key from base64
        secret = base64.b64decode(self.cybersource_secret_key)

        # Create HMAC SHA256 signature
        hash_value = hmac.new(secret, sig_value_utf, hashlib.sha256)
        signature = base64.b64encode(hash_value.digest()).decode('utf-8')

        # Construct the final signature header value
        token = (
            f'keyid="{self.cybersource_api_key_id}", algorithm="HmacSHA256", '
            f'headers="host v-c-date (request-target) digest v-c-merchant-id", '
            f'signature="{signature}"'
        )
        return token

    def make_payment_request(self, payload):
        """Send a payment request to Cybersource."""
        utc_now = datetime.now(pytz.UTC)
        time = utc_now.strftime('%a, %d %b %Y %H:%M:%S GMT')

        payload_bytes = json.dumps(payload).encode('utf-8')
        digest = self._get_digest(payload_bytes)
        signature = self._get_signature('POST', time, digest)

        headers = {
            "host": "apitest.cybersource.com",
            "signature": signature,
            "digest": digest,
            "v-c-merchant-id": self.cybersource_merchant_id,
            "v-c-date": time,
            "Content-Type": "application/json"
        }

        request_target = 'https://apitest.cybersource.com/pts/v2/payments'

        try:
            response = requests.post(request_target, headers=headers, data=payload_bytes)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise UserError(f"Payment processing with Cybersource failed: {str(e)}")

    def process_payment_with_cybersource(self, amount, currency, order_id):
        """Method to process a payment with Cybersource."""
        if not isinstance(order_id, str):
            raise UserError(f"Invalid order_id: {order_id}. It must be a string.")

        payload = {
            "clientReferenceInformation": {
                "code": order_id
            },
            "paymentInformation": {
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "12",
                    "expirationYear": "2031"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "totalAmount": f"{amount:.2f}",
                    "currency": currency
                },
                "billTo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "address1": "1 Market St",
                    "locality": "san francisco",
                    "administrativeArea": "CA",
                    "postalCode": "94105",
                    "country": "US",
                    "email": "test@cybs.com",
                    "phoneNumber": "4158880000"
                }
            }
        }

        response_data = self.make_payment_request(payload)

        # Debugging: Print response data
        print(f"Response Data: {response_data}")

        # Extract status and message from response
        status = response_data.get('status', 'UNKNOWN')
        message = response_data.get('message', 'No message')

        return {
            'status': status,
            'message': message,
            'data': response_data
        }
