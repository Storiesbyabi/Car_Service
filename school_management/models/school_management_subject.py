# # -*- coding: utf-8 -*-

from odoo import models,fields

class SchoolManagementSubject(models.Model):
    _name = 'school.management.subject'
    _description = 'Manage subject for school'

    name = fields.Char()
    department_id = fields.Many2one(comodel_name='school.management.department')
    