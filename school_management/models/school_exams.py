# -*- coding: utf-8 -*-
from odoo import fields,models


class SchoolExams(models.Model):
    """ Managing the exam conducting in this school """
    _name = 'school.exams'
    _description = 'School Exams'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    class_id = fields.Many2one(comodel_name='school.class')
    papers_ids = fields.One2many('school.papers','exams_id')
    students_id = fields.Many2one(comodel_name='school.students')
    class_department_id = fields.Many2one('school.department',related="class_id.department_id")
    is_exam = fields.Boolean()

    def action_add(self):
        self.class_id.student_ids.write({
            'exam_ids': [fields.Command.link(self.id)]
        })
        self.is_exam = True
