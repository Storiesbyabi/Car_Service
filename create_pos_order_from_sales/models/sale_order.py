# -*- coding: utf-8 -*-
from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"


    session_id = fields.Many2one('pos.session',string="POS Session", required=True )
    config_id = fields.Many2one('pos.config')
    orders_id = fields.Many2one('pos.order')
    state = fields.Selection(
        selection_add=[
            ('pac', 'Paid at counter'),
        ])


    def action_confirm(self):
        res = super().action_confirm()
        print(123456)
        lines = []
        for line in self.order_line:
            product = self.env['product.product'].search(
                [('product_tmpl_id', '=', line.product_template_id.id)], limit=1)
            print('product', product)

            lines.append(fields.Command.create({
                'product_id': product.id,
                'qty': line.product_uom_qty,
                'price_unit': line.price_unit,
                'price_subtotal': line.price_subtotal,
                'price_subtotal_incl': line.price_subtotal,
            }))

        self.orders_id = self.env['pos.order'].create({
            'partner_id': self.partner_id.id,
            'company_id': self.env.company.id,
            'session_id': self.session_id.id,
            'lines': lines,
            'amount_tax': 0.0,
            'amount_total': self.amount_untaxed,
            'amount_paid': self.amount_paid,
            'amount_return': 0.0
        })
        return res



    def action_pay_at_counter(self):
        self.config_id =self.session_id.config_id.id
        print(self.config_id)
        return {
            'name': 'Payment Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'pos.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_total_amount':self.amount_untaxed,
                'default_paid_amount':self.amount_paid,
                'default_session_id':self.session_id.id,
                'default_data_ids':self.session_id.payment_method_ids.ids,
            }
        }