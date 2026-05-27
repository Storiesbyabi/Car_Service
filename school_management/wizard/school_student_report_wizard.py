# -*- coding: utf-8 -*-
import io
import json
from odoo import fields,models
from odoo.exceptions import UserError
from odoo.tools import json_default
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class SchoolStudentReportWizard(models.TransientModel):
    _name = 'school.student.report.wizard'
    _description = 'School Student Report'

    student_info = fields.Selection(selection=[
        ('class', 'Class'),
        ('department', 'Department')
    ], default='class')
    class_ids = fields.Many2many('school.class')
    department_ids = fields.Many2many('school.department')

    def action_print(self):
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
        return report

    def action_xlsx_report(self):
        if self.student_info:
            if self.student_info == 'class' and not self.class_ids:
                print('student')
                self.class_ids = self.env['school.class'].search([])

            elif self.student_info == 'department' and not self.department_ids:
                self.department_ids = self.env['school.department'].search([])
            print("Search all")
        else:
            raise UserError('Student Info is empty')
        data = {
            'class_ids': self.class_ids.ids,
            'department_ids':self.department_ids.ids,
            'student_info':self.student_info
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'school.student.report.wizard',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Student Report',
                     },
            'report_type': 'xlsx',
        }
    def get_xlsx_report(self,data,response):
        query = """ select r.firstname,r.phone,r.email,s.admission_number,c.name as class,d.name as dep from school_registration as r
                inner join school_students as s on r.id = s.school_registration_id
                inner join school_class as c on s.current_class_id = c.id
                inner join school_department as d on c.department_id = d.id
                """
        params = []
        if data['student_info'] == 'class':
            classes= data['class_ids']
            query += """ where c.name in  %s"""
            params.append(tuple(classes))
        elif data['student_info'] == 'department':

            department = data['department_ids']
            query += """ where d.id in  %s"""
            params.append(tuple(department))
            print(tuple(department))

        self.env.cr.execute(query,params)
        docs = self.env.cr.dictfetchall()

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '10px', 'align': 'center', 'border': 1}
        )
        subhead = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '15px', 'border': 1})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        sheet.set_row(7,20)
        sheet.set_column(7, 3, 10)
        sheet.set_column(7,4,30)
        sheet.set_column(7, 5, 30)
        row = 8
        sheet.write(7, 2, 'Name', subhead)
        sheet.write(7, 3, 'Phone', subhead)
        sheet.write(7, 4, 'email', subhead)
        sheet.write(7, 5, 'Admission no', subhead)
        if data['student_info'] == 'class':
            sheet.merge_range('C3:K6', 'Class REPORT', head)

            for doc in docs:
                col = 2
                sheet.write(row, col, doc['firstname'], cell_format)
                col += 1
                sheet.write(row, col, doc['phone'], cell_format)
                col += 1
                sheet.write(row, col, doc['email'], cell_format)
                col += 1
                sheet.write(row, col, doc['admission_number'], cell_format)
                row += 1
        else:
            sheet.merge_range('C3:K6', 'Department REPORT', head)
            for doc in docs:
                col = 2
                sheet.write(row, col, doc['firstname'], cell_format)
                col += 1
                sheet.write(row, col, doc['phone'], cell_format)
                col += 1
                sheet.write(row, col, doc['email'], cell_format)
                col += 1
                sheet.write(row, col, doc['admission_number'], cell_format)
                row += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
