# # -*- coding: utf-8 -*-

from odoo import fields,models

class SchoolDepartment(models.Model):
    """ The school department and hod is created  """
    _name = 'school.department'
    _description = 'Description for School'

    name = fields.Char()
    hod_id = fields.Many2one(comodel_name='res.partner')