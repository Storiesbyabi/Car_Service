# -*- coding: utf-8 -*-
from odoo import fields,models


class SchoolPapers(models.Model):
    """ Managing exam papers in school """
    _name = 'school.papers'
    _description = 'Exam paper'

    exams_id = fields.Many2one(comodel_name='school.exams')
    pass_mark = fields.Integer()
    max_mark = fields.Integer()
    subject_department_id = fields.Many2one('school.department',related="exams_id.class_department_id")
    subject_id = fields.Many2one(comodel_name='school.subject',domain="[('department_id','=',subject_department_id)]")