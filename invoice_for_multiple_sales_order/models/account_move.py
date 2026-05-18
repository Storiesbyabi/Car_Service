# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    related_so_to_invoice_ids = fields.Many2many(comodel_name='sale.order',string='So',domain="[('invoice_status','=','to invoice')]")

    @api.onchange('related_so_to_invoice_ids')
    def invoice_lines_data(self):
        so_id = self.related_so_to_invoice_ids.ids

        sale_order_line = self.env['sale.order.line'].search([('order_id','in',so_id)])

        self.invoice_line_ids = [fields.Command.create({
                'product_id': sale_order_line.product_template_id})]
