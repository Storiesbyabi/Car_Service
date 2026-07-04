# # -*- coding: utf-8 -*-

import pprint

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

from odoo.addons.payment.logging import get_payment_logger


_logger = get_payment_logger(__name__)


class PaytrailController(http.Controller):
    _return_url = '/payment/paytrail/return'
    _webhook_url = '/payment/webhook'

    @http.route(_return_url, type='http', methods=['GET'], auth='public')
    def paytrail_return_from_checkout(self, **data):
        """Process the payment data sent by Flutterwave after redirection from checkout.

        :param dict data: The payment data.
        """
        _logger.info("Handling redirection from Flutterwave with data:\n%s", pprint.pformat(data))

        print('checkout')
        print('data',data.get('checkout-status'))
        txnid = data.get('checkout-reference')
        status = data.get('checkout-status')
        print('status', status)
        print('data', txnid)

        tx = self.env['payment.transaction'].search([('reference', '=', txnid)], limit=1)

        print('tx', tx)
        print('tx', tx.read())

        if status == 'ok':
            tx._set_done()
        elif status == 'fail':
            tx._set_canceled()
        elif status == 'pending':
            tx._set_pending()
        else:
            print('Transaction Error'
                  )


        # Redirect the user to the status page.
        return request.redirect('/payment/status')













    # @http.route(
    #     _return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False,
    #     save_session=False
    # )
    # def paytrail_return_from_checkout(self, **data):
    #     """Process the payment data sent by Mollie after redirection from checkout.
    #     The route is flagged with `save_session=False` to prevent Odoo from assigning a new session
    #     to the user if they are redirected to this route with a POST request. Indeed, as the session
    #     cookie is created without a `SameSite` attribute, some browsers that don't implement the
    #     recommended default `SameSite=Lax` behavior will not include the cookie in the redirection
    #     request from the payment provider to Odoo. As the redirection to the '/payment/status' page
    #     will satisfy any specification of the `SameSite` attribute, the session of the user will be
    #     retrieved and with it the transaction which will be immediately post-processed.
    #
    #     :param dict data: The payment data (only `id`) and the transaction reference (`ref`)
    #                       embedded in the return URL.
    #     """
    #     print('checkout')
    #     # _logger.info("handling redirection from Mollie with data:\n%s", pprint.pformat(data))
    #     # self._verify_and_process(data)
    #     # return request.redirect('/payment/status')
    #
    #
    #     data = request.httprequest.args.to_dict()
    #
    #     if request.httprequest.method == 'POST':
    #         data.update(request.httprequest.args.form.to_dict())
    #
    #         txnid = data.get('checkout-reference')
    #         status = data.get('checkout-status')
    #         print('status',status)
    #         print('txnid',txnid)
    #
    #
    #         tx = self.env['payment.transaction'].search([('reference', '=', txnid)],limit=1)
    #
            # if status == 'ok':
            #     tx._set_done()
            # elif status == 'fail':
            #     tx._set_canceled()
            # elif status == 'pending':
            #     tx._set_pending()
            # else:
            #     print('Transaction Error'
            #           )
    #         return request.redirect('/payment/status')




