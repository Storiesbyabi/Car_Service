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

        return super().create(vals)

    def _action_user_creation(self):
        """ A method for automation rule, It will
          create a user when new record is created"""
        if self.firstname and self.email:
            print(444)
            self.status = 'registration'
            student_group = self.env.ref('school_management.student_group_manager')
            user = self.env['res.users'].create({
                'name': self.firstname,
                'login': self.email,
                'email': self.email
            })
            user.write({
                'group_ids': [fields.Command.link(student_group.id)]
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
