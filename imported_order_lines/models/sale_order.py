# -*- coding: utf-8 -*-
from odoo import  models,fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_wizard(self):
        """ When clicking the import btn a wizard will
        be open"""
        return {
            'name': 'Sale Order Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'add.orderline.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            }
        }