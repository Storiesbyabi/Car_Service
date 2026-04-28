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



    def action_register(self):
        """ A Btn action for updating the model school.registration """
        student_id = self.env.context.get('student_id')
        class_id = self.env.context.get('previous_class_id')



        record = self.env['school.registration'].browse(student_id)

        current_class = class_id + 1



        self.env['school.students'].create({
            'school_registration_id': record.id,
            'current_class': current_class
        })

        record.write({
            'firstname':self.firstname,
            'lastname':self.lastname,
            'email':self.email,
            'phone':self.phone,
            'aadhar_number': self.aadhar_number,
            'status':'registration'
        })

