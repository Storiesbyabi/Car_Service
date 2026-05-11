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
    _unique_aadhar = models.Constraint('unique(aadhar_number)', 'The Aadhar number should be unique')

    company_id = fields.Many2one('res.company', default=lambda self: self.env.company,
                                 required=True)
    firstname = fields.Char(required=True)
    lastname = fields.Char()
    father = fields.Char()
    mother = fields.Char()
    communication_address = fields.Char()
    same_as_communication_address = fields.Boolean()
    permanent_address = fields.Char()
    email = fields.Char(required=True)
    phone = fields.Char()
    dob = fields.Date()
    age = fields.Integer(compute='_compute_age')
    gender = fields.Char()
    registration_date = fields.Date(default=date.today())
    photo = fields.Image()
    tc = fields.Image()
    aadhar_number = fields.Char()
    status = fields.Selection(selection=[('draft', 'Draft'), ('registration', 'Registration')],
                              default='draft')
    previous_academic_department_id = fields.Many2one(comodel_name='school.department')
    previous_class_id = fields.Many2one(comodel_name='school.class')
    register_sequence = fields.Char(string="Reference Number", default=lambda self:'New')
    exam_ids = fields.One2many('school.exams', 'students_id', readonly=True)
    events_ids = fields.One2many('school.events','students_id',readonly=True)
    is_student = fields.Boolean()

    @api.model_create_multi
    def create(self, vals):
        """Automatically generate a reference number for each student registration
        when a new record is created and saved."""
        for i in vals:
            if i.get('register_sequence', 'New') == 'New':
                i['register_sequence'] = self.env['ir.sequence'].next_by_code('school.registration')
                print("val",i)
        return super().create(vals)

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

    def action_register(self):
        """ A button action for registration, When
         its triggered a wizard will be opened with the default
         values """

        return {
            'name': 'Register Student',
            'type': 'ir.actions.act_window',
            'res_model': 'school.registration.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'student_id': self.id,
                'default_firstname': self.firstname,
                'default_lastname': self.lastname,
                'default_email': self.email,
                'default_phone': self.phone,
                'default_aadhar_number': self.aadhar_number
            }
        }
