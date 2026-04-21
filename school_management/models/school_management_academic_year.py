# # -*- coding: utf-8 -*-

from odoo import fields,models


class SchoolManagementAcademicYear(models.Model):
    _name = 'school.management.academic.year'
    _description = 'Managing the academic year'

    name = fields.Char()