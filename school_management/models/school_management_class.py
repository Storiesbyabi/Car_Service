# # -*- coding: utf-8 -*-

from odoo import models,fields


class SchoolManagementClass(models.Model):
    _name = 'school.management.class'
    _description = 'Manage class of school'

    name = fields.Char()

    department_id = fields.Many2one(comodel_name='school.management.department')

