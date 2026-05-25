# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError


class SchoolReportWizad(models.TransientModel):
    _name = 'school.report.wizard'
    _description = 'A popup for School Wizard'

    report_type = fields.Selection(selection=[
        ('leave', 'Leave'),
        ('club', 'Club'),
        ('student', 'Student')
    ], default=lambda self: self.env.context.get('report_type'))

    student_leave = fields.Selection(selection=[
        ('class', 'Class'),
        ('student', 'Student')
    ], string='Report Type', default='class')

    type_selection = fields.Selection(selection=[
        ('month', 'Month'),
        ('week', 'Week'),
        ('day', 'Day'),
        ('custom', 'Custom')
    ], string='Date', default='month')

    student_info = fields.Selection(selection=[
        ('class', 'Class'),
        ('department', 'Department')
    ], default='class')

    class_ids = fields.Many2many('school.class')
    club_ids = fields.Many2many('school.clubs')
    department_ids = fields.Many2many('school.department')
    students_ids = fields.Many2many('school.students', string='Students')
    start_date = fields.Date(default=date.today())
    end_date = fields.Date(default=date.today())


    def action_print(self):
        if self.report_type == 'club':
            if self.club_ids:
                report = self.env.ref('school_management.action_club_report').report_action(self)
            else:
                raise UserError('Clubs are empty')

        elif self.report_type == 'student':
            if self.student_info:
                if self.student_info == 'class' and not self.class_ids:
                    self.class_ids = self.env['school.class'].search([])
                    print("action", self.class_ids)
                elif self.student_info == 'department' and not self.department_ids:
                    self.department_ids = self.env['school.department'].search([])
                    print("Search all")
            else:
                raise UserError('Student Info is empty')
        else:
            if self.report_type and self.type_selection:
                if self.student_leave == 'class' and not self.class_ids:
                    print("leave")
                    self.class_ids = self.env['school.class'].search([])
                elif self.student_leave == 'student' or not self.students_ids:
                    self.students_ids = self.env['school.students'].search([])
                report = self.env.ref('school_management.action_leave_report').report_action(self)
            else:
                raise UserError("Fill the details")

        return report
