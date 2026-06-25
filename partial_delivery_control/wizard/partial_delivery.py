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
        group = self.env['res.groups'].browse(237)
        print('group', group)
        partners_ids = self.env['res.users'].search([('id', 'in', group.user_ids.ids)]).partner_id
        print('partners_ids', partners_ids)
        # mail=self.env['mail.notification'].create({'body':'qwee','partner_ids':partners_ids,'message_type':'comment','subtype_id':1,'model':'discuss.channel'})

        self.pick_ids.message_post(
            body="This is an urgent internal notification message.",
            subject="System Alert",
            partner_ids=partners_ids.ids,
            message_type="notification",
            subtype_xmlid="mail.mt_comment",
        )

        # for partner in partners_ids:
        #     partner.message_notify(
        #         body='hellooo',
        #         partner_ids=partners_ids.ids,
        #     )




        # self.pick_ids.activity_schedule(
        #         'mail.mail_activity_data_todo',
        #         user_id=partners_ids,
        #         note='Specify the End date of'
        # )





        # print('mail',mail)
