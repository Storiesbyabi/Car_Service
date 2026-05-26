# -*- coding: utf-8 -*-
import io
import json
from odoo import models, fields
from datetime import date
from odoo.exceptions import UserError
from odoo.tools import date_utils, json_default
from datetime import datetime
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


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
            if not self.club_ids:
                self.club_ids = self.env['school.clubs'].search([])
            report = self.env.ref('school_management.action_club_report').report_action(self)
        elif self.report_type == 'student':
            if self.student_info:
                if self.student_info == 'class' and not self.class_ids:
                    self.class_ids = self.env['school.class'].search([])
                    print("action", self.class_ids)
                elif self.student_info == 'department' and not self.department_ids:
                    self.department_ids = self.env['school.department'].search([])
                    print("Search all")
                report = self.env.ref('school_management.action_student_report').report_action(self)
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

    def action_xlsx_report(self):
        if self.report_type == 'club':
            if not self.club_ids:
                self.club_ids = self.env['school.clubs'].search([])
        elif self.report_type == 'student':
            if self.student_info:
                if self.student_info == 'class' and not self.class_ids:
                    self.class_ids = self.env['school.class'].search([])

                elif self.student_info == 'department' and not self.department_ids:
                    self.department_ids = self.env['school.department'].search([])
                print("Search all")
            else:
                raise UserError('Student Info is empty')


        if self.report_type and self.type_selection:
            if self.student_leave == 'class' and not self.class_ids:
                print("leave")
                self.class_ids = self.env['school.class'].search([])
            elif self.student_leave == 'student' or not self.students_ids:
                self.students_ids = self.env['school.students'].search([])

        else:
            raise UserError("Fill the details")
        data = {
            'class_ids': self.class_ids.ids or None,
            'students_ids': self.students_ids.ids or None,
            'department_ids': self.department_ids.ids or None,
            'club_ids': self.club_ids.ids
        }
        print('data',data)
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'school.report.wizard',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Student Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self,data,response):
        """
        Print the XLSX report
        """
        print('get_xlsx_report')
        query =""" select r.firstname,r.phone,r.email,s.admission_number
        ,l.state as status,l.start_date,l.end_date,l.total_days
        ,c.name as class,d.name as dep from school_registration as r
        inner join school_students as s on r.id = s.school_registration_id
        inner join school_class as c on s.current_class_id = c.id
        inner join school_department as d on c.department_id = d.id
        inner join school_leaves as l on s.id = l.students_id
        """

        params = []
        today = datetime.today().date()


        print('std',data)


            # query += """ where c.name in  """
        #     params.append(classes)
        # else:
        #     students = self.students_ids.ids
        #     print(students)
        #     query += """ where s.id in  %s"""
        #     params.append(students)


        self.env.cr.execute(query, params)
        docs = self.env.cr.dictfetchall()
        print(docs)
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output,{'in_memory':True})
        sheet = workbook.add_worksheet()
        border = workbook.add_format({'border': 1})
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'}
        )
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})

        sheet.merge_range('C3:K6','XLSX REPORT')


        row = 2
        for r in docs:
            col = 1
            for c in r:
                sheet.write(row, col, c['firstname'], border)
                sheet.write(row, col, c['admission_number'], border)
                sheet.write(row, col, c['start_date'], border)
                sheet.write(row, col, c['end_date'], border)
                sheet.write(row, col, c['total_days'], border)
                col += 1
            row +=1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()