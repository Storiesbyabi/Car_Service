# -*- coding: utf-8 -*-
from datetime import date, timedelta
from email.policy import default

from odoo import fields,models


class SchoolLeaves(models.Model):
    _name = 'school.leaves'
    _description = 'School Leaves'

    students_id = fields.Many2one(comodel_name='school.students', required=True,ondelete='cascade' )
    class_id = fields.Many2one(related='students_id.current_class_id')
    start_date = fields.Date(default=date.today())
    end_date = fields.Date(default=date.today())

    total_days = fields.Integer(compute="_compute_total_days")
    half_day = fields.Boolean()
    reason = fields.Char()


    def _compute_total_days(self):
        """ It's used to calculate the total number of business
        days from start_date to end_date and check the week days using
        inbuild weekday() function"""
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date.weekday() < 5:
                self.total_days +=1
            current_date += timedelta(days=1)
