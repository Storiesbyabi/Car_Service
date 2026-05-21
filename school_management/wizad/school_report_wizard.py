 # -*- coding: utf-8 -*-
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
    ])

    class_ids = fields.Many2many('school.class')
    club_ids = fields.Many2many('school.clubs')
    department_ids = fields.Many2many('school.department')

    def action_print(self):
        return self.env.ref('school_management.action_club_report').report_action(self)




