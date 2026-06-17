# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date
from odoo.exceptions import UserError

class PosWizard(models.TransientModel):
    _name = "pos.wizard"

    company_currency_id = fields.Many2one('res.currency', compute='_compute_company_currency_id')
    sale_order_id = fields.Many2one('sale.order')
    total_amount = fields.Monetary(related="sale_order_id.amount_untaxed",currency_field='company_currency_id')
    paid_amount= fields.Float(related="sale_order_id.amount_paid", string='Paid Amount')
    remaining_amount= fields.Monetary(currency_field='company_currency_id',compute='_compute_remaining_amount',store=True)
    session_id = fields.Many2one('pos.session')
    config_id = fields.Many2one('pos.config',related='sale_order_id.session_id.config_id')
    data_ids = fields.Many2many('pos.payment.method')
    wizard_ids = fields.One2many('pos.wizard2', 'wizard_id', string="payment")


    orders_id = fields.Many2one(related='sale_order_id.orders_id')



    def _compute_company_currency_id(self):
        self.company_currency_id = self.env.company.currency_id

    @api.depends('total_amount','paid_amount','wizard_ids.amount','data_ids')
    def _compute_remaining_amount(self):
        self.paid_amount = sum(self.wizard_ids.mapped('amount'))
        for rec in self.wizard_ids:
            print('rec',self.paid_amount)
            print('t', self.total_amount)

            remaining_amount = self.total_amount - self.paid_amount
            if remaining_amount < 0:
                raise UserError('Value error')
            else:
                self.remaining_amount = remaining_amount
            print('r', self.remaining_amount)



    def action_payment(self):
        print('order_id', self.orders_id)
        print('pay_ids', self.sale_order_id)

        for line in self.wizard_ids:

            print('payment method',line.payment_method_id.name)
            print('payment method',line.payment_method_id.id)
            print('amount',line.amount)
            if line.amount <= 0:
                raise UserError('Value cant be 0')
            self.env['pos.payment'].create(
                {
                    'amount': line.amount,
                    'payment_date': date.today(),
                    'payment_method_id': line.payment_method_id.id,
                    'pos_order_id': self.orders_id.id
                }
            )
            order=self.env['pos.order'].browse(self.orders_id.id)
            order.amount_paid += line.amount
            order._compute_prices()
        self.sale_order_id.amount_untaxewizard_idd = self.remaining_amount
        if self.sale_order_id.amount_untaxed == 0:
            self.sale_order_id.state = 'pac'





class PosWizard2(models.TransientModel):
    _name = "pos.wizard2"

    wizard_id=fields.Many2one('pos.wizard')
    payment_method_id = fields.Many2one('pos.payment.method')
    amount = fields.Float(string='Amount',store=True)

