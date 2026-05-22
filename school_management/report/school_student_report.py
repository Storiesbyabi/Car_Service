# -*- coding: utf-8 -*-
from odoo import models,api

class SchoolStudentReport(models.AbstractModel):
    _name = 'report.school_management.report_student_template'
    _description = 'School Report Print'


    @api.model
    def _get_report_values(self, docids,data=None):
        docs = self.env['school.report.wizard'].browse(docids)

        query = """ select r.firstname,r.phone,r.email,s.admission_number,c.name as class,d.name from school_registration as r
        inner join school_students as s on r.id = s.school_registration_id
        inner join school_class as c on s.current_class_id = c.id
        inner join school_department as d on c.department_id = d.id
        """
        params=[]
        if docs.student_info == 'class':
            classes=tuple(docs.class_ids.ids)
            query += """ where c.name in  %s"""
            params.append(classes)
        elif docs.student_info =='department':

            department = tuple(docs.department_ids.ids)
            query += """ where d.id in  %s"""
            params.append(department)
            print(tuple(department))

        self.env.cr.execute(query,params)
        report = self.env.cr.dictfetchall()

        print(report)

        # return {
        #     'doc_ids': docids,
        #     'doc_model': 'school_report_wizard',
        #     'docs': docs,
        # }
