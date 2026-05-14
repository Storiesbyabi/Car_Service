# # -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolRegistrationWizad(models.TransientModel):
    _name = 'school.registration.wizard'
    _description = 'A popup for Registration'

    firstname = fields.Char()
    lastname = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    aadhar_number = fields.Char()
    current_class_id = fields.Many2one(comodel_name="school.class")
    photo = fields.Image()


    def action_register(self):
        """ A Btn action for updating the model school.registration, and
         decoding the image for returning a rainbow man effect"""
        student_id = self.env.context.get('student_id')
        record = self.env['school.registration'].browse(student_id)
        self.env['school.students'].create({
            'school_registration_id': record.id,
            'current_class_id': self.current_class_id.id,
        })
        if self.firstname:
            record.write({
                'firstname': self.firstname,
                'lastname': self.lastname,
                'email': self.email,
                'phone': self.phone,
                'aadhar_number': self.aadhar_number,
            })
            print("Wizard btn")
        effect_image = self.photo.decode('utf-8')

        return {
           'effect': {
               'fadeout': 'slow',
               'message': 'Student is Registered',
                          'type': 'rainbow_man',
               'img_url': f"data:image/jpeg;base64,{effect_image}"
           }
       }
