# # -*- coding: utf-8 -*-

from odoo import api, fields, models


class PartialDeliveryWizard(models.TransientModel):

    _inherit = 'stock.backorder.confirmation'

    approve_flag = fields.Boolean(default=lambda self: self.env.context.get('hide_button'))

    # def _compute_flag(self):
    #     for rec in self:
    #         rec.pick_ids.approve_flag
    #         print('flag',rec.pick_ids.approve_flag)




    def action_request(self):
        print('id',self.backorder_confirmation_line_ids.picking_id.product_id)
        print('context',self.pick_ids.approve_flag)
        print('context1',self.env.context.get('hide_button'))
        print('context2', self.approve_flag)
        self.pick_ids.state = 'not_approval'
        pass

