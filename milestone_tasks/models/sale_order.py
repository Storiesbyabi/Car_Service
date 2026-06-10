# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    flag = fields.Boolean(default=False)
    project_name_id = fields.Many2one('project.project')




    def action_project(self):
        self.flag = True
        milestone_dict = {}
        project_id = self.env['project.project'].create({
            'name': self.name,
            'allow_billable': True,
        })
        self.project_name_id = project_id.id
        for order in self.order_line:
            milestone = order.milestone
            if milestone not in milestone_dict:
                milestone_dict[milestone] = []
            milestone_dict[milestone].append(order.product_template_id.name)
        print(milestone_dict)

        for milestone in milestone_dict:
            parent_task=self.env['project.task'].create({
                'project_id': project_id.id,
                'display_name': f"Milestone{milestone}",
            })
            for product in milestone_dict[milestone]:
                self.env['project.task'].create({
                    'project_id': project_id.id,
                    'parent_id': parent_task.id,
                    'display_name': f"Milestone{milestone}-{product}"
                })

    def action_update_project(self):
        milestone_dict = {}
        print('project_id',self.project_name_id)


        for order in self.order_line:
            milestone = order.milestone
            if milestone not in milestone_dict:
                milestone_dict[milestone] = []
            milestone_dict[milestone].append(order.product_template_id.name)
        print(milestone_dict)

        for milestone in milestone_dict:
            self.project_name_id.write({
                'display_name': f"Milestone{milestone}",
            })
            print(4567,self.project_name_id.task_ids)
            # sub_task=self.env['project.task'].search([('parent_id','in',parent_task)])
            # if sub_task:
            #     print('sub_task',sub_task.ids)
            # print('task_ids',self.project_name_id.task_ids.ids)
            # for product in milestone_dict[milestone]:
            #     self.project_name_id.task_ids.write({
            #         'display_name': f"Milestone{milestone}-{product}"
            #     })
