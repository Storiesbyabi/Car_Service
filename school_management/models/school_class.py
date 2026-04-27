# # -*- coding: utf-8 -*-
""" School class can be managed in this model"""
from odoo import models,fields


class SchoolClass(models.Model):
    """ The school class and department is created and managed   """
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(help="class name")
    department_id = fields.Many2one(comodel_name='school.department')
    head_of_dep_id = fields.Many2one( related='department_id.hod_id')
    school_id = fields.Many2one('res.company',default=lambda self: self.env.company
                                 )
