# -*- coding: utf-8 -*-

from odoo import fields, models


class RfqWizard(models.Model):
    _name = 'rfq.wizard'

    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    product_id = fields.Many2one('product.template',readonly=True)


    def action_confirm(self):
        vendor = self.product_id.variant_seller_ids.partner_id

        purrchase_order = self.env['purchase.order'].search([('partner_id','=',vendor[-1]),('state','=','draft')],limit=1)

        if purrchase_order:
            self.env['purchase.order.line'].write({
                'product_id':self.product_id,
                'product_qty':self.quantity,
                'price_unit':self.price
            })
            print('Updated')
        else:
            self.env['purchase.order.line'].create({
                'product_id': self.product_id,
                'product_qty': self.quantity,
                'price_unit': self.price
            })
            print('Created')




