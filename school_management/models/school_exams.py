# -*- coding: utf-8 -*-
from odoo import fields,models


class SchoolExams(models.Model):
    """ Managing the exam conducting in this school """
    _name = 'school.exams'
    _description = 'School Exams'

    name = fields.Char(string='Exam Name')
    class_id = fields.Many2one(comodel_name='school.class')
    papers_ids = fields.One2many('school.subject','exams_id')
