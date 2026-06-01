# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'
    # user_list = []

    @api.constrains('user_ids')
    def check_limit(self):
        """ To validate the user task count
         and raise a ValidationError. If the
         user count is equal to 0 an unlimited
         task can be assigned"""
        users = self.user_ids.ids
        print('user_ids', users)
        for user in users:
            count = self.env['project.task'].search_count([('user_ids','=',user)])
            user_i = self.env['res.users'].browse(user)
            print('out count',count)
            print('user_count',user_i.task_count)
            if user_i.task_count == 0:
                continue
            if count > user_i.task_count:
                print('user', user)
                raise ValidationError('User Exceed the Limit')


    # def check_group(self):
    #     if self.env.user.has_groups('limit_no_open_task.admin'):
    #         if self.stage_id.name == 'New':
    #             self.flag = False
    #             print('flag', self.stage_id.name)
    #     else:
    #         self.flag = True

    # def action_approve(self):
    #     self.set_user = True
    #     self.user_ids = self.env['res.users'].browse(self.user_list)
    #     print('approve',self.user_ids)
