# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta, date


class SchoolEvents(models.Model):
    """ To Manage School Events in School """
    _name = 'school.events'
    _description = 'School events'
    _inherit = 'mail.thread'

    name = fields.Char(string="School Event", required=True)
    clubs_id = fields.Many2one(comodel_name="school.clubs")
    date_begin = fields.Date()
    date_end = fields.Date(required=True)
    organizer_id = fields.Many2one(comodel_name="res.partner")
    poster = fields.Image()
    description = fields.Char()
    status = fields.Selection(selection=[('draft','Draft'),('scheduled','Scheduled'),('ongoing','Ongoing'),('ended','Ended'),('cancel','Canceled')],default='draft')
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(comodel_name='res.partner')


    def action_confirm(self):
        """ Btn action for changing the status to
          scheduled and ongoing based on condition"""
        for record in self:
            if record.status == 'draft':
                record.status = 'scheduled'
            else:
                record.status = 'ongoing'


    def action_cancel(self):
        """ Btn action for changing the status to cancel """
        for record in self:
            record.status = 'cancel'

    def action_end(self):
        """ Btn action for changing the status to ended """
        for record in self:
            record.status = 'ended'


    @api.onchange('date_begin')
    def _invite(self):
        for i in self:
            days = i.date_begin - timedelta(days=2)
            if date.today() == days:
                mail_template = self.env.ref('school_management.email_template')
                mail_template.send_mail(self.id,force_send=False)
                print("Triggered")


