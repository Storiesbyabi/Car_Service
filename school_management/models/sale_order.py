# -*- coding: utf-8 -*-
from odoo import fields,models


class SaleOrder(models.Model):
    """ Add new state admitted to the
    existing state in sales module"""
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('admitted', 'Admitted')])
