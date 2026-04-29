# -*- coding: utf-8 -*-
from odoo import fields,models


class SaleOrder(models.Model):
    """ Inherited from sales Module """
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('admitted', 'Admitted')])


