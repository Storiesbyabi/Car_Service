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


    def _get_redirect_form_view(self,is_validation=False):

        self.redirect_form_view_id = self.env.ref('payment_paytrail.redirect_form')
        print('id',self.redirect_form_view_id)

        return super()._get_redirect_form_view(is_validation=False)
