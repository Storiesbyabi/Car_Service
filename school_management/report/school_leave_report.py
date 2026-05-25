# -*- coding: utf-8 -*-
from odoo import models, api
from datetime import datetime, timedelta

from odoo.exceptions import UserError


class SchoolLeaveReport(models.AbstractModel):
    _name = 'report.school_management.report_leave_template'
    _description = 'Leave Report Print'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['school.report.wizard'].browse(docids)

        query = """ select r.firstname,r.phone,r.email,s.admission_number
        ,l.state as status,l.start_date,l.end_date,l.total_days
        ,c.name as class,d.name as dep from school_registration as r
        inner join school_students as s on r.id = s.school_registration_id
        inner join school_class as c on s.current_class_id = c.id
        inner join school_department as d on c.department_id = d.id
        inner join school_leaves as l on s.id = l.students_id
        """
        params = []
        today = datetime.today().date()
        if docs.student_leave == 'class':
            classes = tuple(docs.class_ids.ids)
            query += """ where c.name in  %s"""
            params.append(classes)
        else:
            students = tuple(docs.students_ids.ids)
            print(students)
            query += """ where s.id in  %s"""
            params.append(students)
            print(students)
        if docs.type_selection == 'month':
            print('month', today.strftime('%m'))
            query += """ and TO_CHAR(l.start_date, 'MM') =  %s"""
            params.append(today.strftime('%m'))

        elif docs.type_selection == 'day':
            print('day', today.strftime('%d'))
            query += """ and TO_CHAR(l.start_date, 'DD') =  %s"""
            params.append(today.strftime('%d'))
        elif docs.type_selection == 'custom':
            if docs.start_date:
                query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD') between %s and %s"""
                params.append(str(docs.start_date))
                params.append(str(docs.end_date))
            else:
                print('ssdfdsfdsf')
                query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD')  <= %s """
                params.append(str(docs.end_date))

        elif docs.type_selection == 'week':
            start_week = today - timedelta(days=today.weekday())
            end_week = start_week + timedelta(days=6)
            query += """ and TO_CHAR(l.start_date, 'YYYY-MM-DD') between %s and %s"""
            start_str = start_week.strftime('%Y-%m-%d')
            end_str = end_week.strftime('%Y-%m-%d')

            params.append(start_str)
            params.append(end_str)
            print(222, start_str, end_str)
        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        print(report)

        return {
            'doc_ids': docids,
            'doc_model': 'school_report_wizard',
            'docs': docs,
            'report': report
        }