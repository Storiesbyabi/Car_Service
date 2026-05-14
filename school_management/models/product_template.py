# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'


    def action_rfq_wizard(self):
        print("Wizard")
        return {
            'name':'Purchase Order',
            'type': 'ir.actions.act_window',
            'res_model': 'rfq.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': self.id,
                'default_seller_ids':self.seller_ids

            }
        }