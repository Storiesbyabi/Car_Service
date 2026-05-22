from flake8.formatting import default  # -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolReportWizad(models.TransientModel):
    _name = 'school.report.wizard'
    _description = 'A popup for School Wizard'

    report_type = fields.Selection(selection=[
        ('leave','Leave'),
        ('club','Club'),
        ('student','Student')
    ],default= lambda self: self.env.context.get('report_type'))

    student_leave = fields.Selection(selection=[
        ('class','Class'),
        ('student','Student')
    ],string='Report Type')

    type_selection = fields.Selection(selection=[
        ('month','Month'),
        ('week','Week'),
        ('day','Day'),
        ('custom','Custom')
    ],string='Date')

    student_info = fields.Selection(selection=[
        ('class','Class'),
        ('department','Department')
    ],required=True,default='class')

    class_ids = fields.Many2many('school.class')
    club_ids = fields.Many2many('school.clubs')
    department_ids = fields.Many2many('school.department')

    @api.onchange('')

    def action_print(self):
        if self.report_type == 'club':
            report = self.env.ref('school_management.action_club_report').report_action(self)
        elif self.report_type == 'student':
            if self.student_info=='class' and not self.class_ids:
                self.class_ids = self.env['school.class'].search([])
                print("action",self.class_ids)
            # elif self.student_info=='department' and not self.department_ids:
            #     self.department_ids = self.env['school.department'].search([])
            print("action", self.department_ids)

            report = self.env.ref('school_management.action_student_report').report_action(self)
        return report
