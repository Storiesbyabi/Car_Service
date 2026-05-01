# # -*- coding: utf-8 -*-
from odoo import models,fields


class SchoolSubject(models.Model):
    """ The school subject is created  """
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char()
    department_id = fields.Many2one(comodel_name='school.department')
    exams_id = fields.Many2one(comodel_name='school.exams')
    pass_mark = fields.Integer()
    max_mark = fields.Integer()
