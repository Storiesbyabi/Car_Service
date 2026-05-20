# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    related_so_to_invoice_ids = fields.Many2many(comodel_name='sale.order',string='So',
                                                 domain="[('invoice_status','=','to invoice'),('partner_id','=',partner_id)]")
    invoice_line = fields.One2many('account.move.line',
        'move_id',compute='_invoice_lines_data',store=True,readonly=False)

    @api.depends('related_so_to_invoice_ids')
    def _invoice_lines_data(self):
        """ It's used to create invoice lines based on
         related sale order, also create invoice lines
         and linked to the SO"""
        if self.state == 'draft':
            invoice_lines = []
            for so in self.related_so_to_invoice_ids:
                for line in so.order_line:
                    invoice_lines.append(
                        fields.Command.create({
                            'product_id': line.product_id.id,
                            'sale_line_ids': [fields.Command.link(line.id)]
                        })
                    )
            print('invoice', invoice_lines)
            self.invoice_line_ids = invoice_lines
            print('invoice lines', self.invoice_line_ids)

    # @api.onchange('related_so_to_invoice_ids')
    # def invoice_lines_data(self):
    #     invoice_lines = []
    #     for so in self.related_so_to_invoice_ids:
    #         for line in so.order_line:
    #
    #             invoice_lines.append(
    #                 fields.Command.create({
    #                     'product_id':line.product_id.id,
    #                     'sale_line_ids':[fields.Command.link(line.id)]
    #                 })
    #             )
    #
    #     print('invoice',invoice_lines)
    #     self.invoice_line_ids = invoice_lines
    #     print('invoice lines', self.invoice_line_ids)
