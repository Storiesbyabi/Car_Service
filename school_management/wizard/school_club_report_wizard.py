# -*- coding: utf-8 -*-
import io
import json
from odoo import fields,models
from datetime import date
from odoo.tools import json_default

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter

class SchoolClubReportWizard(models.TransientModel):
    _name = 'school.club.report.wizard'
    _description = 'School Club Report'

    club_ids = fields.Many2many('school.clubs')

    def action_print(self):
        if not self.club_ids:
            self.club_ids = self.env['school.clubs'].search([])
        report = self.env.ref('school_management.action_club_report').report_action(self)
        return report

    def action_xlsx_report(self):
        if not self.club_ids:
            self.club_ids = self.env['school.clubs'].search([])
        data={
            'club_ids':self.club_ids.ids
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'school.club.report.wizard',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Club Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self,data,response):
        print('std', data)
        clubs = data['club_ids']
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '10px', 'align': 'center', 'border': 1}
        )
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        subhead = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '15px','border': 1,})
        printformat = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '13px'})
        dateformat = workbook.add_format(
            {'font_size': '10px', 'align': 'center'}
        )
        today = date.today()
        today = str(today)
        sheet.merge_range('C3:K6', 'Clubs REPORT', head)

        row = 10
        sheet.set_column(7, 0, 15)
        sheet.write(7, 0, 'Print Date:', printformat)
        sheet.write(7, 1, today, dateformat)
        sheet.set_row(9, 20)
        sheet.set_column(9, 4, 15)
        sheet.write(9,2,'Sl No',subhead)
        sheet.write(9,3,'Club',subhead)
        sheet.write(9,4,'Name',subhead)
        sheet.write(9,5,'Ad No',subhead)
        sheet.write(9,6,'Class',subhead)
        sheet.write(9,7,'School',subhead)
        sl = 1
        for o in clubs:
            d = self.env['school.clubs'].browse(o)
            col = 2
            sheet.write(row, col, sl, cell_format)
            col += 1
            sheet.write(row, col, d.name, cell_format)
            col += 1
            sheet.write(row, col, d.students_ids.firstname, cell_format)
            col += 1
            sheet.write(row, col, d.students_ids.admission_number, cell_format)
            col += 1
            sheet.write(row, col, d.students_ids.current_class_id.name, cell_format)
            col += 1
            sheet.write(row, col, d.students_ids.company_id.name, cell_format)
            sl +=1
            row += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
