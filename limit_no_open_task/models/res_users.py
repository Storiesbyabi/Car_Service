# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    task_count = fields.Integer(default=1)