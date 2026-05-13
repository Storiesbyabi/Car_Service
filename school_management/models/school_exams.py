# -*- coding: utf-8 -*-
from odoo import fields,models, api


class SchoolExams(models.Model):
    """ Managing the exam conducting in this school """
    _name = 'school.exams'
    _description = 'School Exams'
    _inherit = 'mail.thread'

    name = fields.Char(required=True)
    class_id = fields.Many2one(comodel_name='school.class')
    papers_ids = fields.One2many('school.papers','exams_id')
    students_id = fields.Many2one(comodel_name='school.students')

    def action_add(self):
        self.class_id.student_ids.write({
            'exam_ids': [fields.Command.link(self.id)]
        })

    @api.onchange('class_id')
    def subject(self):
        subject_id = self.papers_ids.subject_id.id
        domain = [(subject_id,'=',self.class_id.department_id.id)]
        print("domain",domain)

        return {
            'domain':{'papers_ids':domain}
        }