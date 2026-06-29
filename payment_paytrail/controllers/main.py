# # -*- coding: utf-8 -*-

import pprint

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

from odoo.addons.payment.logging import get_payment_logger


_logger = get_payment_logger(__name__)


class MollieController(http.Controller):
    _return_url = '/payment/paytrail/return'
    _webhook_url = '/payment/paytrail/webhook'
