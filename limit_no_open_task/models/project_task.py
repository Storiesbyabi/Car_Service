# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = 'project.task'



    @api.onchange('user_ids')
    def check_limit(self):
        users = self.user_ids.ids
        for user in users:
            count = self.env['project.task'].search_count([('user_ids','=',user)])
            count +=1
            user_i = self.env['res.users'].browse(user)
            print('out count',count)
            print('user_count',user_i.task_count)
            if count > user_i.task_count:
                raise UserError('User has attained the limit')
    # @api.model_create_multi
    # def create(self,val_list):
    #     for val in val_list:
    #         users = val.get('user',self.user_ids)
    #         print('user',users)
        # users = self.user_ids.ids
        # for user in users:
        #     count = self.env['project.task'].search_count([('user_ids', '=', user)])
        #     count += 1
        #     user_i = self.env['res.users'].browse(user)
        #     print('out count', count)
        #     print('user_count', user_i.task_count)
        #     if count > user_i.task_count:
        #         raise UserError('User has attained the limit')
        #         return {'type': 'ir.actions.act_window_close'}