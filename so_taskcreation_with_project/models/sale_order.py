# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    related_project_id = fields.Many2one('project.project')


    def action_task(self):
        print('product',self.order_line.product_template_id.name)
        print('quanty',self.order_line.product_uom_qty)


        parent_task=self.env['project.task'].create({
            'project_id': self.related_project_id.id,
            'display_name': f"SO/{self.name}-{self.partner_id.name}",
            'description': f"Order Date:{self.date_order}",
            'user_ids': self.user_id,

        })

        for line in self.order_line:
            self.env['project.task'].create({
                'parent_id': parent_task.id,
                'project_id': self.related_project_id.id,
                'display_name': f"{line.product_template_id.name}-Qty:{line.product_uom_qty}",
            })

    def action_smart_btn(self):
        task_ids = self.related_project_id.task_ids
        for task in task_ids:
            print('display name',task.display_name)
            task_name = task.display_name
        return{
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'list',
            'domain': [('id','in',task_ids.ids)],
        }

