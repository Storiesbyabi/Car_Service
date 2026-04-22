# -*- coding: utf-8 -*-
from datetime import date
from odoo import fields, models, api
class SchoolRegistration(models.Model):
    """The new student is registered here"""
    _name = 'school.registration'
    _description = 'School registration management'
    _inherit = 'mail.thread'
    _rec_name = 'register_sequence'

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
    registration_date = fields.Date(default=date.today())
    photo = fields.Image()
    tc = fields.Image()
    aadhar_number = fields.Integer()
    status = fields.Selection(selection=[('draft','Draft'), ('registration','Registration')])
    previous_academic_department_id = fields.Many2one(comodel_name='school.department')
    previous_class_id = fields.Many2one(comodel_name='school.class')
    register_sequence = fields.Char(string="Reference Number",default= lambda self: 'New')

    @api.model_create_multi
    def create(self,vals):
        """Automaticaly generate a reference number for each student registration
        when a new record is created and saved."""
        for i in vals:
            if i.get('register_sequence', 'New') == 'New':
                i['register_sequence'] = self.env['ir.sequence'].next_by_code('school.registration')
        return super(SchoolRegistration, self).create(vals)
