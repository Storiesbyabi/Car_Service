# # -*- coding: utf-8 -*-
from odoo import models, fields


class SchoolClubs(models.Model):
    """ To manage the clubs in the school """
    _name = 'school.clubs'
    _description = 'School Clubs'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    students_ids = fields.Many2many('school.students',ondelete="cascade")


    def action_event(self):
        """ To filter the events based on clubs"""
        return {
            'name':'Events',
            'type':'ir.actions.act_window',
            'res_model': 'school.events',
            'view_mode':'list,form',
            'domain':[('clubs_id','=',self.id)]
        }
