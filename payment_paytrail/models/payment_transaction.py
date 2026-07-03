# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug.urls import url_decode, url_parse

from odoo import _, api, models
from odoo.exceptions import ValidationError
from odoo.tools import urls
from odoo.addons.payment.logging import get_payment_logger
from datetime import datetime, timezone
from uuid import uuid4
from encodings.utf_8 import encode
import hashlib
import hmac
import json
from hmac import HMAC
import requests






_logger = get_payment_logger(__name__)


class PaymentTransaction(models.Model):
    _return_url = '/payment/paytrail'
    _webhook_url = '/payment/webhook'
    _inherit = 'payment.transaction'

    @staticmethod
    def compute_sha256_hash(message: str, secret: str) -> str:

        # whitespaces that were created during json parsing process must be removed
        hash = hmac.new(secret.encode(), message.encode(), digestmod=hashlib.sha256)
        return hash.hexdigest()

    # /
    # @param secret Merchant shared secret
    # @param headerParams Headers or query string parameters
    # @param body Request body or empty string for GET request
    # @return
    # /
    def calculate_hmac(self, secret: str, headerParams: dict, body: str = '') -> str:

        data = []
        for key, value in headerParams.items():
            if key.startswith('checkout-'):
                data.append('{key}:{value}'.format(key=key, value=value))

        data.append(body)
        return self.compute_sha256_hash('\n'.join(data), secret)






    def _get_specific_processing_values(self, processing_values):
        """ Override of payment to redirect pending token-flow transactions.

        If the financial institution insists on 3-D Secure authentication, this
        override will redirect the user to the provided authorization page.
        Note: `self.ensure_one()`
    """
        if self.provider_code != 'paytrail':
            return super()._get_specific_processing_values(processing_values)
        print('processing',processing_values)
        print(1,self.operation)
        print(2,self.provider_id.redirect_form_view_id)

        return {'redirect_form_html': self.env['ir.qweb']._render(
            self.provider_id.redirect_form_view_id.id
        )}





    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return Flutterwave-specific rendering values.

        Note: self.ensure_one() from `_get_processing_values`

        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of provider-specific processing values.
        :rtype: dict
        """
        print('processing',processing_values)
        print(123213213321)
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'paytrail':
            return res

        payload = self._paytrail_prepare_payment_request_payload()

        dt_now = datetime.now(timezone.utc)
        secret = "SAIPPUAKAUPPIAS"

        z_timestamp = dt_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # print(z_timestamp)

        headers = ({
            'checkout-account': '375917',
            'checkout-algorithm': 'sha256',
            'checkout-method': 'POST',
            'checkout-nonce': f"{uuid4()}",
            'checkout-timestamp': f"{z_timestamp}",

        })

        body = json.dumps(payload, separators=(',', ':'))
        print('body', body)
        encData = self.calculate_hmac(secret, headers, body)
        print('encData', encData)
        headers['signature'] = encData


        try:
            response = requests.request(
                'POST','https://services.paytrail.com/payments', data=body,headers=headers,
                timeout=10,
            )
            response.raise_for_status()
            res_json = response.json()
            print('res', res_json)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            raise ValidationError(_("Could not establish the connection to the payment provider."))
        res_data = res_json.get('href')
        return {'api_url':res_data}



    def _paytrail_prepare_payment_request_payload(self):
        """ Create the payload for the payment request based on the transaction values.

        :return: The request payload
        :rtype: dict
        """
        user_lang = self.env.context.get('lang')
        return_url = f"{self.get_base_url()}/payment/paytrail/return"
        # redirect_url = urls.urljoin(base_url, _return_url)
        # webhook_url = urls.urljoin(base_url, _webhook_url)

        return {
            "stamp": f"{uuid4()}",
            "reference": "9187445",
            "amount": int(self.amount*100),
            "currency": "EUR",
            "language": "EN",
            "items": [
                {
                    "unitPrice": int(self.amount*100),
                    "units": 1,
                    "vatPercentage": 0,
                    "productCode": "#927502759",
                    "stamp": f"{uuid4()}"
                }
            ],
            "customer": {
                "email": "erja.esimerkki@example.org"
            },
            "redirectUrls": {
                "success": return_url,
                "cancel": return_url,
            },

        }



    # def _apply_updates(self, payment_data):
    #     """Override of `payment` to update the transaction based on the payment data."""
    #     if self.provider_code != 'paytrail':
    #         return super()._apply_updates(payment_data)
    #
    #     # Update the payment method.
    #     payment_method_type = payment_data.get('method', '')
    #     if payment_method_type == 'creditcard':
    #         payment_method_type = payment_data.get('details', {}).get('cardLabel', '').lower()
    #     payment_method = self.env['payment.method']._get_from_code(
    #         payment_method_type, mapping=const.PAYMENT_METHODS_MAPPING
    #     )
    #     self.payment_method_id = payment_method or self.payment_method_id
    #
    #     # Update the payment state.
    #     payment_status = payment_data.get('status')
    #     if payment_status in ('pending', 'open'):
    #         self._set_pending()
    #     elif payment_status == 'authorized':
    #         self._set_authorized()
    #     elif payment_status == 'paid':
    #         self._set_done()
    #     elif payment_status in ['expired', 'canceled', 'failed']:
    #         self._set_canceled(_("Cancelled payment with status: %s", payment_status))
    #     else:
    #         _logger.info(
    #             "Received data with invalid payment status (%s) for transaction %s.",
    #             payment_status, self.reference
    #         )
    #         self._set_error(_("Received data with invalid payment status: %s.", payment_status))

    # def _get_specific_rendering_values(self, processing_values):
    #     """ Override of payment to return Mollie-specific rendering values.
    #
    #     Note: self.ensure_one() from `_get_processing_values`
    #
    #     :param dict processing_values: The generic and specific processing values of the transaction
    #     :return: The dict of provider-specific rendering values
    #     :rtype: dict
    #     """
    #     print('val',processing_values)
    #     if self.provider_code != 'paytrail':
    #         return super()._get_specific_rendering_values(processing_values)
    #
    #     payload = self._paytrail_prepare_payment_request_payload()
    #     try:
    #         payment_data = self._send_api_request('POST', 'https://services.paytrail.com/payments', json=payload)
    #     except ValidationError as error:
    #         self._set_error(str(error))
    #         return {}
    #
    #     # The provider reference is set now to allow fetching the payment status after redirection
    #     self.provider_reference = payment_data.get('id')
    #
    #     # Extract the checkout URL from the payment data and add it with its query parameters to the
    #     # rendering values. Passing the query parameters separately is necessary to prevent them
    #     # from being stripped off when redirecting the user to the checkout URL, which can happen
    #     # when only one payment method is enabled on Mollie and query parameters are provided.
    #     checkout_url = self._return_url
    #     parsed_url = url_parse(checkout_url)
    #     url_params = url_decode(parsed_url.query)
    #     # redirect_form_html= self.env['ir.qweb']._render(
    #     #     self.provider_id.redirect_form_view_id.id)
    #     return {'api_url': checkout_url, 'url_params': url_params}