# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ApprovalWizard(models.TransientModel):
    _name = 'approval.wizard'

    def action_approve(self):
        pass