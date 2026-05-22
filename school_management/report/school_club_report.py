# -*- coding: utf-8 -*-
from odoo import models,api

class SchoolClubReport(models.AbstractModel):
    _name = 'report.school_management.report_club_template'
    _description = 'School Report Print'


    @api.model
    def _get_report_values(self, docids,data=None):
        docs = self.env['school.report.wizard'].browse(docids)

        # print(docs.club_ids.students_ids.firstname)

        return {
            'doc_ids': docids,
            'doc_model': 'school_report_wizard',
            'docs': docs,
        }
