# # -*- coding: utf-8 -*-

from odoo import models,fields


class SchoolClass(models.Model):
    """ The school class and department is created and managed   """
    _name = 'school.class'
    _description = 'Manage class of school'

    name = fields.Char()

    department_id = fields.Many2one(comodel_name='school.department')

