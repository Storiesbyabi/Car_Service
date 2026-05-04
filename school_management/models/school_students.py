# -*- coding: utf-8 -*-
from email.policy import default

from odoo import fields,models,api
from odoo.orm.decorators import readonly


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
    exam_ids = fields.One2many('school.exams','students_id',readonly=True)


    @api.model_create_multi
    def create(self, vals):
        """Automatically generate an admission number for each student registration
        when a new record is registered     ."""
        for i in vals:
            if i.get('admission_number', 'new') == 'new':
                i['admission_number'] = self.env['ir.sequence'].next_by_code('school.registration.admission')
        return super().create(vals)


    @api.depends('admission_number','firstname')
    def _compute_display_name(self):
        """ Combine the admission number and first name of the student
         and display in the _rec_name """
        for record in self:
            if record.admission_number:
                record.display_name = f"{record.admission_number}{record.firstname}"
            else:
                record.display_name = record._name

    def action_register(self):
        """ To avoid action error in btn """
        pass