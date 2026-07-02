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



# def _build_request_url(self, endpoint, **kwargs):
#     """Override of `payment` to build the request URL."""
#     if self.code != 'paytrail':
#         return super()._build_request_url(endpoint, **kwargs)
#     print('request url')
#     return url_join('https://services.paytrail.com', endpoint)
#
# def _build_request_headers(self, *args, **kwargs):
#     print('hii')
#     """Override of `payment` to build the request headers."""
#     if self.code != 'paytrail':
#         return super()._build_request_headers(*args, **kwargs)
#
#     dt_now = datetime.now(timezone.utc)
#     secret = "SAIPPUAKAUPPIAS"
#
#     z_timestamp = dt_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#     # print(z_timestamp)
#
#     print('args', *args)
#     headers =({
#         'checkout-account': '375917',
#         'checkout-algorithm': 'sha256',
#         'checkout-method': 'POST',
#         'checkout-nonce': f"{uuid4()}",
#         'checkout-timestamp': f"{z_timestamp}",
#
#     })
#
#     body = json.dumps(*args, separators=(',', ':'))
#     print('body', body)
#     encData = self.calculate_hmac(secret, headers, body)
#     print('encData', encData)
#     headers['signature']=encData
#     return headers

