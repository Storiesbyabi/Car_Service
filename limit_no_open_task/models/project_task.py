# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    flag = fields.Boolean(default=True,compute='check_group')

    @api.constrains('user_ids')
    def check_limit(self):
        users = self.user_ids.ids
        for user in users:
            count = self.env['project.task'].search_count([('user_ids','=',user)])
            user_i = self.env['res.users'].browse(user)
            print('out count',count)
            print('user_count',user_i.task_count)
            if user_i.task_count == 0:
                continue
            if count > user_i.task_count:
                return {
                    'res_model': 'project.approve',
                    'context': {
                        'default_task_id': self.id,},
                }
            else:
                self.can_edit = True


    def check_group(self):
        if self.env.user.has_groups('limit_no_open_task.admin'):
            if self.stage_id.name == 'New':
                self.flag = False
                print('flag', self.stage_id.name)
        else:
            self.flag = True

    def action_approve(self):
        pass
