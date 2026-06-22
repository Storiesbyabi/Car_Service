# # -*- coding: utf-8 -*-

from odoo import api, fields, models

class Product(models.Model):
    _inherit = "product.template"

    allow_partial_delivery = fields.Boolean(string="Allow Partial Delivery")