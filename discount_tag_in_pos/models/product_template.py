# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    discount_tag = fields.Char(string="Discount Tag")

    @api.model
    def _load_pos_data_fields(self, config_id):
        """
        Adds the 'discount_tag' field to the list of fields loaded into the POS.
        """
        data = super()._load_pos_data_fields(config_id)
        data += ['discount_tag']
        return data
