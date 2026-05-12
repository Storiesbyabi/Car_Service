# # -*- coding: utf-8 -*-
""" The academic year is managed in this module  """
from odoo import fields,models


class SchoolManagementAcademicYear(models.Model):
    """The School academic year is created """
    _name = 'school.academic.year'
    _description = 'Academic year'

    name = fields.Char(required=True)