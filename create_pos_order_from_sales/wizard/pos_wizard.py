# -*- coding: utf-8 -*-
from odoo import fields, models

class PosWizard(models.TransientModel):
    _name = "pos.wizard"

    company_currency_id = fields.Many2one('res.currency', compute='_compute_company_currency_id')
    sale_order_id = fields.Many2one('sale.order')

    total_amount = fields.Monetary(related="sale_order_id.amount_total",currency_field='company_currency_id')
    paid_amount= fields.Float(related="sale_order_id.amount_paid")
    remaining_amount= fields.Monetary(default=0,currency_field='company_currency_id')
    session_id = fields.Many2one(related="sale_order_id.session_id")
    pos_payment_id = fields.Many2one('pos.payment.method')






    def _compute_company_currency_id(self):
        self.company_currency_id = self.env.company.currency_id

    def action_payment(self):
        print('id',self.sale_order_id)
        print('amount',self.total_amount)

