# # -*- coding: utf-8 -*-

from odoo import fields,models

class SchoolManagementDepartment(models.Model):
    _name = 'school.management.department'
    _description = 'Description for School'

    name = fields.Char()
    hod_id = fields.Many2one(comodel_name='res.partner')