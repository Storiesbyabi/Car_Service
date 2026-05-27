# -*- coding: utf-8 -*-
from odoo import fields, models


class RfqWizard(models.TransientModel):
    """ A wizard for automating the rfq to
     Purchase order through action_confirm btn"""
    _name = 'rfq.wizard'

    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    product_id = fields.Many2one('product.template', readonly=True)

    def action_confirm(self):
        """ An automatic purchase order will be created for
          vendor who has no rfq and update the vendor order lines
           who have a rfq"""
        vendor = self.product_id.variant_seller_ids.partner_id
        print('vendor',vendor[-1].id)
        purchase_order = (self.env['purchase.order'].search(
            [('partner_id', 'in', vendor[-1].id),('state', '=', 'draft')],
            limit=1))
        product_varient = self.env['product.product'].search(
            [('product_tmpl_id','=',self.product_id.id)])
        print('varient',product_varient)
        print(4444,purchase_order)
        print("product",self.product_id.id)

        if purchase_order:
            self.env['purchase.order.line'].create({
                'product_id': product_varient.id,
                'product_qty': self.quantity,
                'price_unit': self.price,
                'order_id':purchase_order.id,
                'state':'purchase'
            })
            print('Updated')
        else:
            order = self.env['purchase.order'].create({
                'partner_id':vendor[-1].id,
            })
            print("order id",order.id)
            self.env['purchase.order.line'].create({
                'product_id': product_varient.id,
                'product_qty': self.quantity,
                'price_unit': self.price,
                'order_id':order.id,
                'state': 'purchase'
            })
            print('Created')
