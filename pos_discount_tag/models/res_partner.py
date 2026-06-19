# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    limit = fields.Boolean(string="Order Limit")
    limit_amount = fields.Integer(string="Limit Amount")
    customer_limit = fields.Integer(string="Customer Limit")


    @api.model
    def _load_pos_data_fields(self, config_id):
        """
        Adds the 'limit_amount' field to the list of fields loaded into the POS.
        """
        data = super()._load_pos_data_fields(config_id)
        data += ['limit_amount','customer_limit']
        return data
