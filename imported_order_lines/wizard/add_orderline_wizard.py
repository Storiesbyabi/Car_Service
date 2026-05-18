# -*- coding: utf-8 -*-
from odoo import fields, models
import openpyxl
import base64
from io import BytesIO


class AddOrderlineWizard(models.TransientModel):
    """ Create sale order line from xls using openpyxl"""
    _name = 'add.orderline.wizard'
    _description = 'Add sale order line'

    file = fields.Binary(string='File', required=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order')

    def action_import(self):
        data = base64.b64decode(self.file)
        stream = BytesIO(data)
        wb = openpyxl.load_workbook(
            filename=stream, data_only=True
        )
        ws = wb.active

        order_lines = []

        for col in ws.iter_rows(min_row=2, max_row=None, min_col=None, values_only=True):
            product_name = col[0]
            product_quantity = col[1]
            product_unit = col[2] or 'Units'
            product_description = col[3]
            product_price = col[4]

            if product_unit == 'Units':
                units = self.env.ref('uom.product_uom_unit')
            else:
                units = self.env['uom.uom'].search([('name','=',product_unit)])

            order_lines.append({
                'product_name': product_name,
                'product_quantity': product_quantity or 1,
                'product_unit': units.id,
                'product_description': product_description or product_name,
                'product_price': product_price or 1
            })
        print("order_lines", order_lines)
        for product in order_lines:
            print('product name', product['product_name'])

            product_id = self.env['product.product'].search(
                [('display_name', '=', product['product_name'])], limit=1
            )

            if not product_id:
                product_id = self.env['product.product'].create({
                    'name': product['product_name'],
                    'description': product['product_description'],
                    'lst_price': product['product_price']
                })
            print('product_id', product_id)

            print("sale order", self.sale_order_id)

            self.sale_order_id.order_line = [fields.Command.create({
                'product_id': product_id.id,
                'product_uom_id': product['product_unit'],
                'product_uom_qty': product['product_quantity'],
                'name': product['product_description'],
                'price_unit': product['product_price']
            })]
           
