# # -*- coding: utf-8 -*-

from odoo import api, fields, models


class PartialDeliveryWizard(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    approve_flag = fields.Boolean(default=lambda self: self.env.context.get('hide_button'))


    def action_request(self, ):
        print('id', self.backorder_confirmation_line_ids.picking_id.product_id)
        print('context', self.pick_ids.approve_flag)
        print('context1', self.env.context.get('hide_button'))
        print('context2', self.approve_flag)
        # self.pick_ids.state = 'not_approval'
        group = self.env['res.groups'].browse(236)
        print('group', group)
        partners_ids = self.env['res.users'].search([('id', 'in', group.user_ids)]).partner_id.ids
        print('user', users)
        # mail=self.env['mail.notification'].create({'body':'qwee','partner_ids':partners_ids,'message_type':'comment','subtype_id':1,'model':'discuss.channel'})

        # thread = self.env['mail.thread']
        #
        # thread.message_post(
        #     body="This is an urgent internal notification message.",
        #     subject="System Alert",
        #     partner_ids=partners_ids,
        #     message_type="notification",
        #     subtype_xmlid="mail.mt_comment"
        # )

        # print('mail',mail)
