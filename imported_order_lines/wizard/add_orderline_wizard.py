# -*- coding: utf-8 -*-

from odoo import fields, models
import openpyxl
import base64
from io import BytesIO


class AddOrderlineWizard(models.TransientModel):
    _name = 'add.orderline.wizard'
    _description = 'Add sale order line'

    file = fields.Binary(string='File',required=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order')


    def action_import(self):
        wb = openpyxl.load_workbook(
            filename=BytesIO(base64.b64decode(self.file)), read_only=True
        )

        ws = wb.active

        order_lines = []

        for col in ws.iter_rows(min_row=2, max_row=None, min_col=None):
            product_template = col[0]
            product_quantity = col[1]
            product_unit = col[2]
            product_description = col[3]
            product_price = col[4]

            order_lines.append({
                'product_template':product_template,
                'product_quantity':product_quantity,
                'product_unit':product_unit,
                'product_description':product_description,
                'product_price':product_price
            })

        print("order_lines",order_lines)

        for product in order_lines:

            order = self.env['sale.order.line'].search(
                [('order_id','=',self.sale_order_id.id)]
            )

            if order:
                self.env['sale.order.line'].write(
                    {
                        'product_uom_qty':product['product_quantity'],
                        'price_unit':product['product_price']
                    }
                )
            else:
                self.env['sale.order.line'].create({
                    'product_template_id':product['product_template'],
                    'product_uom_id':product['product_unit'],
                    'product_uom_qty': product['product_quantity'],
                    'name':product['product_description'],
                    'price_unit': product['product_price']
                })





