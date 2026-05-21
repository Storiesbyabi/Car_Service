# -*- coding: utf-8 -*-
from odoo import models,api

class SchoolReportPrint(models.AbstractModel):
    _name = 'report.school_management.report_club_template'
    _description = 'School Report Print'


    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['school.report.wizard'].browse(docids)
        query = """ select * from school_clubs """
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        print(report)
