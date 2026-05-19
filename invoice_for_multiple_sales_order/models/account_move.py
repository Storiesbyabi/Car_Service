# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    related_so_to_invoice_ids = fields.Many2many(comodel_name='sale.order',string='So',domain="[('invoice_status','=','to invoice'),('partner_id','=',partner_id)]")

    @api.onchange('related_so_to_invoice_ids')
    def invoice_lines_data(self):
        so_id = self.related_so_to_invoice_ids

        print('sale order',so_id)

        sale_order_id = so_id.order_line
        print(sale_order_id)

        if sale_order_id:
            for i in sale_order_id.product_id.ids:
                self.invoice_line_ids = [fields.Command.create({
                    'product_id': i

                })]
                for i in self.invoice_line_ids.ids:
                    print(i)
                    so_id.order_line.invoice_lines = [fields.Command.link(
                        i
                    )]
            self.move_type = 'out_invoice'

            print('move_type',self.move_type)



            print(22,self.invoice_line_ids.ids)

            print('invoice_ids',so_id.order_line.invoice_lines)








