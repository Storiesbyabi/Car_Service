# -*- coding: utf-8 -*-
from odoo import fields,models,api


class ResPartner(models.Model):
    """ Inherited from Res partner Module """
    _inherit = 'res.partner'
    _unique_name = models.Constraint('unique(complete_name)', 'Its must be unique')
    _unique_email = models.Constraint('unique(email)', 'Its must be unique')

    partner_selection = fields.Selection(selection=[('teacher','Teacher'),('student','Student'),
                                          ('office_staff','Office Staff')], string='Partner')
