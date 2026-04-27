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
        context = self.env.context
        print(context)
