# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = "project.task"

    sl_id = fields.Many2one('sale.order.line')