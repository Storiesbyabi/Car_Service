# -*- coding: utf-8 -*-
from odoo import fields,models,api


class SchoolStudents(models.Model):
    """ The Registered students are managed  """
    _name = 'school.students'
    _description = 'Inherits of Registration'
    _inherit = 'mail.thread'
    _inherits = {'school.registration':'school_registration_id'}


    school_registration_id = fields.Many2one(comodel_name='school.registration', required=True, ondelete="cascade")
    admission_number = fields.Char(string='Admission Number', default='new')
    compute_rec_name = fields.Char(compute='_compute_fields_combination')
    current_class_id = fields.Many2one(comodel_name="school.class")
    clubs_ids = fields.Many2many(comodel_name='school.clubs')
    is_student = fields.Boolean(default=True)
    exam_ids = fields.One2many('school.exams','students_id',readonly=True)
    std_status = fields.Selection(selection=[('absent','Absent'),('present','Present')],default='present')


    @api.model_create_multi
    def create(self, vals):
        """Automatically generate an admission number for each student registration
        when a new record is registered. """
        for val in vals:
            print("val",val)
            if val.get('admission_number', 'new') == 'new':
                val['admission_number'] = self.env['ir.sequence'].next_by_code('school.registration.admission')
            # user_name = val.get('firstname')
            # user_email = val.get('email')

        return super().create(vals)

    def _action_user_creation(self):
        """ A method for automation rule, It will
          create a user when new record is created"""
        for record in self:
            if record.firstname and record.email:
                print(444)
                record.status = 'registration'
                self.env['res.users'].create({
                    'name': record.firstname,
                    'login': record.email,
                    'email': record.email
                })


    @api.depends('admission_number','firstname')
    def _compute_display_name(self):
        """ Combine the admission number and first name of the student
         and display in the _rec_name """
        for record in self:
            if record.admission_number:
                record.display_name = f"{record.admission_number} {record.firstname}"
            else:
                record.display_name = record._name

    def action_register(self):
        """ To change the status of new record
         to registration"""
        pass
