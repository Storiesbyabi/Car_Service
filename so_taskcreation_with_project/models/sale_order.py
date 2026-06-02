# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    related_project_id = fields.Many2one('project.project')

    def action_task(self):
        # print('product',self.order_line.product_template_id.name)
        # print('quanty',self.order_line.product_uom_qty)
        task_ids = self.related_project_id.task_ids

        a = []

        for s in self.order_line:
            a.append(s.price_subtotal)
        amount = max(a)
        print('list',amount)


        if not task_ids:
            parent_task = self.env['project.task'].create({
                'project_id': self.related_project_id.id,
                'display_name': f"SO/{self.name}-{self.partner_id.name}",
                'description': f"Order Date:{self.date_order}",
                'user_ids': self.user_id,

            })


            for line in self.order_line:
                priority = ''
                if line.price_subtotal == amount:
                    priority = '3'
                else:
                    priority = '0'

                self.env['project.task'].create({
                    'priority': priority,
                    'parent_id': parent_task.id,
                    'project_id': self.related_project_id.id,
                    'display_name': f"{line.product_template_id.name}-Qty:{line.product_uom_qty}",
                })
        else:
            raise UserError('Task already exists')


    def action_smart_btn(self):
        task_ids = self.related_project_id.task_ids
        print('task_ids',task_ids.ids)
        print('subtask',task_ids.child_ids.ids)
        return{
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'list,form',
            'domain': [('id','in',task_i0ds.ids)],
        }

