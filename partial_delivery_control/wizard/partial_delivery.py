# # -*- coding: utf-8 -*-

from odoo import api, fields, models


class PartialDeliveryWizard(models.TransientModel):

    _inherit = 'stock.backorder.confirmation'

    def action_request(self):
        print('id',self.pick_ids)
        self.pick_ids.state = 'not_approval'
        pass
