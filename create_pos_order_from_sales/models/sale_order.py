# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"


    session_id = fields.Many2one('pos.session',string="POS Session", required=True )
    config_id = fields.Many2one('pos.config')

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
                'default_total_amount':self.amount_total,
                'default_paid_amount':self.amount_paid,
            }
        }