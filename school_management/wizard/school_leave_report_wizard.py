# -*- coding: utf-8 -*-
import io
import json
from odoo import models, fields
from datetime import date
from odoo.exceptions import UserError
from odoo.tools import  json_default
from datetime import datetime, timedelta

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class SchoolLeaveReportWizad(models.TransientModel):
    _name = 'school.leave.report.wizard'
    _description = 'A popup for School Wizard'

    class_ids = fields.Many2many('school.class')
    students_ids = fields.Many2many('school.students', string='Students')
    student_leave = fields.Selection(selection=[
        ('class', 'Class'),
        ('student', 'Student')
    ], string='Leave Type', default='class')

    type_selection = fields.Selection(selection=[
        ('month', 'Month'),
        ('week', 'Week'),
        ('day', 'Day'),
        ('custom', 'Custom')
    ], string='Date', default='month')
    start_date = fields.Date(default=date.today())
    end_date = fields.Date(default=date.today())

    def action_print(self):
        if self.student_leave and self.type_selection:
            if self.student_leave == 'class' and not self.class_ids:
                print("leave")
                self.class_ids = self.env['school.class'].search([])
            elif self.student_leave == 'student' and not self.students_ids:
                print('search all students')
                self.students_ids = self.env['school.students'].search([])
            else:
                raise UserError("Fill the details")
            report = self.env.ref('school_management.action_leave_report').report_action(self)
        return report

    def action_xlsx_report(self):
        if self.student_leave and self.type_selection:
            if self.student_leave == 'class' and not self.class_ids:
                print("leave")
                self.class_ids = self.env['school.class'].search([])
            elif self.student_leave == 'student' and not self.students_ids:
                self.students_ids = self.env['school.students'].search([])
        else:
            raise UserError("Fill the details")
        data = {
            'class_ids': self.class_ids.ids ,
            'students_ids': self.students_ids.ids,
            'student_leave': self.student_leave
        }
        print('data', data)
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'school.leave.report.wizard',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        """
        Print the XLSX report
        """
        print('get_xlsx_report')
        query = """ select r.firstname,r.phone,r.email,s.admission_number
                ,l.state as status,l.start_date::text,l.end_date::text,l.total_days
                ,c.name as class,d.name as dep from school_registration as r
                inner join school_students as s on r.id = s.school_registration_id
                inner join school_class as c on s.current_class_id = c.id
                inner join school_department as d on c.department_id = d.id
                inner join school_leaves as l on s.id = l.students_id
                """
        params = []
        today = datetime.today().date()
        print('std', data)
        print('response',self)
        print('status',data['student_leave'])
        if data['student_leave'] == 'class':
            classes = data['class_ids']
            query += """ where c.name in  %s"""
            params.append(tuple(classes))
            print('params',params)
        else:
            students = data['students_ids']
            print('students',students)
            query += """ where s.id in  %s"""
            params.append(tuple(students))
        if self.type_selection == 'month':
            print('month', today.strftime('%m'))
            query += """ and TO_CHAR(l.start_date, 'MM') =  %s"""
            params.append(today.strftime('%m'))

        elif self.type_selection == 'day':
            print('day', today.strftime('%d'))
            query += """ and TO_CHAR(l.start_date, 'DD') =  %s"""
            params.append(today.strftime('%d'))
        elif self.type_selection == 'custom':
            if self.start_date:
                query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD') between %s and %s"""
                params.append(str(self.start_date))
                params.append(str(self.end_date))
            else:
                print('ssdfdsfdsf')
                query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD')  <= %s """
                params.append(str(self.end_date))

        elif self.type_selection == 'week':
            start_week = today - timedelta(days=today.weekday())
            end_week = start_week + timedelta(days=6)
            query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD') between %s and %s"""
            start_str = start_week.strftime('%Y-%m-%d')
            end_str = end_week.strftime('%Y-%m-%d')

            params.append(start_str)
            params.append(end_str)
            print(222, start_str, end_str)
        self.env.cr.execute(query, params)
        docs = self.env.cr.dictfetchall()
        print('docs',docs)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '10px', 'align': 'center','border': 1}
        )
        subhead = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '15px', 'border': 1})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        row = 8
        sheet.set_row(7,20)
        if data['student_leave'] == 'class':
            sheet.merge_range('C3:K6', 'Class REPORT', head)
            sheet.set_column(7,4,15)
            sheet.set_column(7,5,15)
            sheet.write(7, 2, 'Name', subhead)
            sheet.write(7, 3, 'Ad No', subhead)
            sheet.write(7, 4, 'Start', subhead)
            sheet.write(7, 5, 'End', subhead)
            sheet.write(7, 6, 'Total', subhead)
            for r in docs:
                col = 2
                sheet.write(row, col, r['firstname'], cell_format)
                col += 1
                sheet.write(row, col, r['admission_number'], cell_format)
                col += 1
                sheet.write(row, col, r['start_date'], cell_format)
                col += 1
                sheet.write(row, col, r['end_date'], cell_format)
                col += 1
                sheet.write(row, col, r['total_days'], cell_format)
                row += 1
        elif data['student_leave'] == 'student':
            sheet.merge_range('C3:K6', 'Student REPORT', head)
            sheet.set_column(7, 3, 15)
            sheet.set_column(7, 4, 15)
            sheet.write(7, 2, 'Ad No', subhead)
            sheet.write(7, 3, 'Start', subhead)
            sheet.write(7, 4, 'End', subhead)
            sheet.write(7, 5, 'Total', subhead)
            sheet.write(7, 6, 'Email', subhead)
            for r in docs:
                col = 2
                sheet.write(row, col, r['admission_number'], cell_format)
                col += 1
                sheet.write(row, col, r['start_date'], cell_format)
                col += 1
                sheet.write(row, col, r['end_date'], cell_format)
                col += 1
                sheet.write(row, col, r['total_days'], cell_format)
                col += 1
                sheet.write(row, col, r['email'], cell_format)
                row +=1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
