# # -*- coding: utf-8 -*-
from addons.web.controllers import domain
from odoo import fields, models, api


class SchoolManagement(models.Model):
    """cfffxfgff"""
    _name = 'school.management'
    _description = 'School management'

    firstname = fields.Char()
    lastname = fields.Char()
    father = fields.Char()
    mother = fields.Char()
    communication_address = fields.Char()
    same_as_communication_address = fields.Boolean()
    permanent_address = fields.Char()
    email = fields.Char()
    phone = fields.Integer()
    dob = fields.Date()
    gender = fields.Char()
    registration_date = fields.Date()
    photo = fields.Image()


    tc = fields.Image()
    aadhar_number = fields.Integer()
    status = fields.Selection(selection=[('draft','Draft'), ('registration','Registration')])

    previous_academic_department = fields.Many2one(comodel_name='school.management.department')
    previous_class = fields.Many2one(comodel_name='school.management.class')
