# -*- coding: utf-8 -*-
""" Module for student registration """
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api
class SchoolRegistration(models.Model):
    """The new student is registered here"""
    _name = 'school.registration'
    _description = 'School registration'
    _inherit = 'mail.thread'
    _rec_name = 'register_sequence'
    _unique_aadhar = models.Constraint('unique(aadhar_number)','The Aadhar number should be unique')

    company_id = fields.Many2one('res.company', default=lambda self: self.env.company,
                                 required=True)
    students_id = fields.Many2one('school.students')
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
    age = fields.Integer(compute='_compute_age')
    gender = fields.Char()
    registration_date = fields.Date(default=date.today())
    photo = fields.Image()
    tc = fields.Image()
    aadhar_number = fields.Char()
    status = fields.Selection(selection=[('draft','Draft'), ('registration','Registration')],
                              default='draft')
    previous_academic_department_id = fields.Many2one(comodel_name='school.department')
    previous_class_id = fields.Many2one(comodel_name='school.class')
    register_sequence = fields.Char(string="Reference Number",default= lambda self: 'New')
    admission_number = fields.Char(string='Admission Number', default= lambda self:'Ad')

    @api.model_create_multi
    def create(self,vals):
        """Automaticaly generate a reference number for each student registration
        when a new record is created and saved."""
        for i in vals:
            if i.get('register_sequence', 'New') == 'New':
                i['register_sequence'] = self.env['ir.sequence'].next_by_code('school.registration')
        return super().create(vals)

    def action_register(self):
        """ A button action for registration, When it is triggered the status
         will be updated to registration and a new admission sequence
         will be generated"""
        for record in self:
            record.status='registration'
            if record.status == 'registration':
                record.admission_number = (self.env['ir.sequence'].next_by_code
                                           ('school.registration.admission'))
                print(record.admission_number)

    @api.depends('dob')
    def _compute_age(self):
        """ The age is calculated based on the give dob and current date,
        The relative delta will calculate the difference and the
        year is stored inside the age"""
        for record in self:
            if record.dob:
                delta = relativedelta(date.today(), record.dob)
                record.age = delta.years
            else:
                record.age = 0
