# -*- coding: utf-8 -*-
from odoo import fields,models


class SchoolExams(models.Model):
    """ Managing the exam conducting in this school """
    _name = 'school.exams'
    _description = 'School Exams'
    _inherit = 'mail.thread'

    name = fields.Char()
    class_id = fields.Many2one(comodel_name='school.class')
    papers_ids = fields.One2many('school.papers','exams_id')
    students_id = fields.Many2one(comodel_name='school.students')

    def action_add(self):
        students = self.env['school.students'].search([('current_class_id','=',self.class_id.id)])
        if students:
            for student in students:
                student.write({
                    'exam_ids':[(4,self.id)]
                })
