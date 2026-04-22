# # -*- coding: utf-8 -*-

from odoo import fields,models


class SchoolManagementAcademicYear(models.Model):
    """The School academic year is created """
    _name = 'school.academic.year'
    _description = 'Managing the academic year'

    name = fields.Char()