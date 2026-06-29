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


    # === REQUEST HELPERS === #

    def _build_request_url(self, endpoint, **kwargs):
        """Override of `payment` to build the request URL."""
        if self.code != 'paytrail':
            return super()._build_request_url(endpoint, **kwargs)
        return urls.urljoin('services.paytrail.com/', endpoint.strip('/'))

    def _build_request_headers(self, *args, **kwargs):
        """Override of `payment` to build the request headers."""
        if self.code != 'paytrail':
            return super()._build_request_headers(*args, **kwargs)


        return {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.mollie_api_key}',
            'Content-Type': 'application/json',

        }

    def _parse_response_error(self, response):
        """Override of `payment` to parse the error message."""
        if self.code != 'paytrail':
            return super()._parse_response_error(response)

        return response.json().get('detail', '')
