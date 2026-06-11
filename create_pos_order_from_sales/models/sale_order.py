# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"


    session_id = fields.Many2one('pos.session',string="POS Session", required=True )

    def action_pay_at_counter(self):
        return {
            'name': 'Payment Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'pos.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_total_amount':self.amount_total,
                'default_paid_amount':self.amount_paid,
                'default_remaining_amount':0,
            }
        }