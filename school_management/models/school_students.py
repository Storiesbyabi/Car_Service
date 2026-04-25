# -*- coding: utf-8 -*-
from odoo import fields,models
from odoo.orm.decorators import readonly


class SchoolStudents(models.Model):
    """ The Registered students are managed  """
    _name = 'school.students'
    _inherit = 'mail.thread'
    _inherits = {'school.registration':'school_registration_id'}

    school_registration_id = fields.Many2one(comodel_name='school.registration', required=True, ondelete="cascade")
    chatter_id = fields.Many2one(comodel_name='mail.thread', required=True, ondelete="cascade")




