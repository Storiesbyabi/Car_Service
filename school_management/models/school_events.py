# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta, date
from odoo.orm.fields_relational import Many2one


class SchoolEvents(models.Model):
    """ To Manage School Events in School """
    _name = 'school.events'
    _description = 'School events'
    _inherit = 'mail.thread'

    name = fields.Char( required=True)
    clubs_id = fields.Many2one(comodel_name="school.clubs")
    date_begin = fields.Date()
    date_end = fields.Date(required=True)
    organizer_id = fields.Many2one(comodel_name="res.partner")
    poster = fields.Image()
    description = fields.Char()
    status = fields.Selection(selection=[('draft','Draft'),('scheduled','Scheduled'),('ongoing','Ongoing'),('ended','Ended'),('cancel','Canceled')],default='draft')
    active = fields.Boolean(default=True)
    partner_id = Many2one(comodel_name='res.partner', domain="[('partner_selection', '=', 'teacher')]")
    students_id = Many2one(comodel_name='school.registration')


    def action_confirm(self):
        """ Btn action for changing the status to
          scheduled and ongoing based on condition"""
        for record in self:
            if record.status == 'draft':
                record.status = 'scheduled'

            students = self.env['school.students'].search([('clubs_ids', '=', self.clubs_id.id)])
            if students:
                for student in students:
                    print("student",student)
                    student.write({
                        'events_ids': [(4, self.id)]
                    })

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
            record.active = False


    @api.model
    def _send_event_reminder(self):
        """ Send an email to the employees before 2 days of event.
         Also decode the image and pass through the context to the
         email template """
        target_days = date.today() + timedelta(days=2)
        records = self.search([('date_begin', '=', target_days)])
        template = self.env.ref('school_management.email_template', raise_if_not_found=False)
        partners = self.env['res.partner'].search([('partner_selection', '=', 'teacher')])
        partners_email = ','.join(partners.mapped('email'))
        for record in records:
            poster_img = record.poster
            poster_img = poster_img.decode('utf-8')
            template.with_context(poster=poster_img).send_mail(record.id, force_send=False, email_values={'email_to':partners_email})

