# # -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolRegistrationWizad(models.TransientModel):
    _name = 'school.registration.wizard'
    _description = 'A popup for Registration'

    firstname = fields.Char()
    lastname = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    aadhar_number = fields.Char()
    current_class_id = fields.Many2one(comodel_name="school.class")



    def action_register(self):
        """ A Btn action for updating the model school.registration """
        student_id = self.env.context.get('student_id')
        record = self.env['school.registration'].browse(student_id)
        self.env['school.students'].create({
            'school_registration_id': record.id,
            'current_class_id': self.current_class_id.id
        })
        print(self.current_class_id.id)
        record.write({
            'firstname':self.firstname,
            'lastname':self.lastname,
            'email':self.email,
            'phone':self.phone,
            'aadhar_number': self.aadhar_number,
            'status':'registration'
        })
