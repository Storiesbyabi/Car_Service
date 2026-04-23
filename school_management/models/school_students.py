# -*- coding: utf-8 -*-

from odoo import fields,models

class SchoolStudents(models.Model):
    """ The Registered students are managed  """
    _name = 'school.students'
    _description = 'School Students'

    name = fields.Char()



