# -*- coding: utf-8 -*-
from datetime import date, timedelta
from odoo import fields,models, api


class SchoolLeaves(models.Model):
    _name = 'school.leaves'
    _description = 'School Leaves'
    _rec_name = 'students_id'
    _inherit = 'mail.thread'


    students_id = fields.Many2one(comodel_name='school.students', required=True,ondelete='cascade' )
    class_id = fields.Many2one(related='students_id.current_class_id')
    start_date = fields.Date(default=date.today())
    end_date = fields.Date(default=date.today())
    total_days = fields.Float(compute="_compute_total_days",store=True)
    half_day = fields.Boolean()
    reason = fields.Char()
    is_leave = fields.Boolean()
    state = fields.Selection(selection=[('draft','Draft'),('confirm','Confirm')],default='draft')

    @api.depends('start_date','end_date','half_day')
    def _compute_total_days(self):
        """ It's used to calculate the total number of business
        days from start_date to end_date and check the week days using
        inbuild weekday() function"""
        for record in self:
            current_date = record.start_date
            record.total_days = 0
            while current_date <= record.end_date:
                if current_date.weekday() < 5:
                    record.total_days += 1
                current_date += timedelta(days=1)
            if record.half_day:
                record.start_date = record.end_date
                record.total_days = 0.5

    def action_confirm(self):
        if self.state == 'draft':
               self.write(
                {
           'state': 'confirm',
            'is_leave' :True
                }
            )

    @api.model
    def _student_leave(self):
        std = self.students_id.id
        student = self.env['school.students'].browse(std)
        start = self.start_date
        end = self.end_date
        today = date.today()

        if self.state == 'confirm':
            while start <= end:
                if start == today:
                    student.std_status = 'absent'
                start += timedelta(days=1)

