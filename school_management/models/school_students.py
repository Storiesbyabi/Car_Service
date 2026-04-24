# -*- coding: utf-8 -*-
from odoo import fields,models

class SchoolStudents(models.Model):
    """ The Registered students are managed  """
    _name = 'school.students'
    _inherit = 'school.registration'

    school_registration_id = fields.Many2one(comodel_name='school.registration')
    admission_number = fields.Char(related='school_registration_id.admission_number')
    previous_class_id = fields.Many2one(related='school_registration_id.previous_class_id')

