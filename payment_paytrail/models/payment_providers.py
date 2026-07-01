from odoo import _, fields, models, service
from odoo.tools import urls


from odoo.addons.payment.logging import get_payment_logger



_logger = get_payment_logger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('paytrail', 'Paytrail')], ondelete={'paytrail': 'set default'}
    )

    merchant_id = fields.Char(string='Merchant ID', required_if_provider='paytrail',)
    secret_key = fields.Char(string='Secret Key', required_if_provider='paytrail',)


    def _build_request_url(self, endpoint, **kwargs):
        """Override of `payment` to build the request URL."""
        if self.code != 'paytrail':
            return super()._build_request_url(endpoint, **kwargs)
        print('request url')
        return url_join('https://services.paytrail.com', endpoint)

    def _build_request_headers(self, *args, **kwargs):
        """Override of `payment` to build the request headers."""
        if self.code != 'paytrail':
            return super()._build_request_headers(*args, **kwargs)


        print('args',*args)



        return {'Authorization': f'Bearer {self.flutterwave_secret_key}'}


























    def _build_request_url(self, endpoint, **kwargs):
        """Override of `payment` to build the request URL."""
        if self.code != 'paytrail':
            return super()._build_request_url(endpoint, **kwargs)
        return 'https://services.paytrail.com/payments'


    def _build_request_headers(self, *args, **kwargs):
        """Override of `payment` to build the request headers."""
        if self.code != 'paytrail':
            return super()._build_request_headers(*args, **kwargs)
        print('id',self.merchant_id)
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'checkout-account': self.merchant_id,
            'checkout-algorithm':'sha256',
            'checkout-method':'POST',
            'checkout-nonce':'123123',
            'checkout-timestamp':'2018-07-05T11:19:25.950Z',
        }



    def _parse_response_error(self, response):
        """Override of `payment` to parse the error message."""
        if self.code != 'paytrail':
            return super()._parse_response_error(response)

        return response.json().get('detail', '')
