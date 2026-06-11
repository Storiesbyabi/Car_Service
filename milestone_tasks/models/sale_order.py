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
        })
        self.project_name_id = project_id.id
        for order in self.order_line:
            milestone = order.milestone
            if milestone not in milestone_dict:
                milestone_dict[milestone] = {}
            milestone_dict[milestone][order.id] = order.product_template_id.name

        print('milestone',milestone_dict)




        for milestone in milestone_dict:
            parent_task=self.env['project.task'].create({
                'project_id': project_id.id,
                'display_name': f"Milestone{milestone}",
            })
            print('milestone',milestone)
            for product in milestone_dict[milestone]:
                print('product', milestone_dict[milestone][product])
                print('id',product)
                self.env['project.task'].create({
                    'sl_id':product,
                    'project_id': project_id.id,
                    'parent_id': parent_task.id,
                    'display_name': f"Milestone{milestone}-{milestone_dict[milestone][product]}"
                })


    def action_update_project(self):
        # self.flag=False
        milestone_dict = {}
        print('project_id',self.project_name_id)

        for order in self.order_line:
            milestone = order.milestone
            if milestone not in milestone_dict:
                milestone_dict[milestone] = {}
            milestone_dict[milestone][order.id] = order.product_template_id.name

        print('milestone', milestone_dict)

        parent_task=self.env['project.task'].search([('project_id','=',self.project_name_id),('parent_id','=',False)])

        print('parent_task',parent_task)

        for line in self.order_line:
            sub_task_id = self.env['project.task'].search([('sl_id', '=',line.id)])

            print('prd',milestone_dict.get(line.milestone)[line.id])
            sub_task_id.write({
                'display_name': f"Milestone{line.milestone}-{milestone_dict.get(line.milestone)[line.id]}",
            })

            print('name',sub_task_id.parent_id.name)
            # if sub_task_id.parent_id.name != f"Milestone{line.milestone}":
            #     sub_task_id.parent_id.write({
            #         'name':f"Milestone{line.milestone}"
            #     })


            print('sub_task_id',sub_task_id.display_name)


        sub_task = parent_task.child_ids
        print('sub_task',sub_task)

        # for task in parent_task:
        #     print('task', task)
        #     task_id = task.child_ids
        #     for sub in task_id:
        #         print('sub', sub)








            # sub_task=self.env['project.task'].search([('parent_id','in',parent_task)])
            # if sub_task:
            #     print('sub_task',sub_task.ids)
            # print('task_ids',self.project_name_id.task_ids.ids)
            # for product in milestone_dict[milestone]:
            #     self.project_name_id.task_ids.write({
            #         'display_name': f"Milestone{milestone}-{product}"
            #     })
