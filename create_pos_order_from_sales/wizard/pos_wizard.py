# -*- coding: utf-8 -*-
from docutils.frontend import store_multiple
from odoo import fields, models, api
from datetime import date

class PosWizard(models.TransientModel):
    _name = "pos.wizard"

    company_currency_id = fields.Many2one('res.currency', compute='_compute_company_currency_id')
    sale_order_id = fields.Many2one('sale.order')
    total_amount = fields.Monetary(related="sale_order_id.amount_total",currency_field='company_currency_id')
    paid_amount= fields.Float(related="sale_order_id.amount_paid", string='Paid Amount')
    remaining_amount= fields.Monetary(currency_field='company_currency_id',compute='_compute_remaining_amount',store=True)
    session_id = fields.Many2one(related="sale_order_id.session_id")
    pos_name_id = fields.Many2one('pos.config', related="session_id.config_id")
    payment_method_id = fields.Many2one('pos.payment.method')

    wizard_ids = fields.One2many('pos.wizard2', 'wizard_id', string="payment")



    def _compute_company_currency_id(self):
        self.company_currency_id = self.env.company.currency_id

    @api.depends('total_amount','paid_amount','wizard_ids.amount')
    def _compute_remaining_amount(self):
        for rec in self.wizard_ids:
            total_am = self.total_amount
            print('t', self.total_amount)
            self.paid_amount += rec.wizard_ids.amount
            self.remaining_amount = self.total_amount - self.wizard_ids.amount
            print('r', self.remaining_amount)


    def action_payment(self):
        self.paid_amount = self.amount

        lines=[]

        for line in self.sale_order_id.order_line:
            product = self.env['product.product'].search([('product_tmpl_id','=',line.product_template_id.id)])
            print('product',product)
        #     lines.append(fields.Command.create({
        #         'product_id':product.id,
        #         'qty':line.product_uom_qty,
        #         'price_unit':line.price_unit,
        #     }))
        #
        # order_id=self.env['pos.order'].create({
        #     'partner_id': self.sale_order_id.partner_id.id,
        #     'company_id': self.env.company.id,
        #     'session_id': self.session_id.id,
        #     'lines':lines,
        #     'amount_tax': 0.0,
        #     'amount_total':self.total_amount,
        #     'amount_paid':self.amount
        # })
        for line in self.wizard_ids:
            print('payment method',line.payment_method_id.name)
            print('amount',line.amount)
        # self.env['pos.payment'].create(
        #     {
        #         'amount': 100,
        #         'payment_date': date.today(),
        #         'payment_method_id': self.payment_method_id.id,
        #         'pos_order_id': order_id.id
        #     }
        # )



class PosWizard2(models.TransientModel):
    _name = "pos.wizard2"

    wizard_id=fields.Many2one('pos.wizard')
    payment_method_id = fields.Many2one('pos.payment.method')
    amount = fields.Float(string='Amount',store=True)

