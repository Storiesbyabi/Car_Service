# # -*- coding: utf-8 -*-

from odoo import fields,models,api

class EstatePropertyType(models.Model):
    _name= 'estate.property.type'
    _description = 'The Property type for estate'
    _rec_name = 'property_type'
    _order = 'property_type'
    _unique_property_name = models.Constraint('unique(property_type)','Its must be unique')

    property_ids = fields.One2many('estate.property','property_type_id')

    property_type=fields.Char()

    offer_ids = fields.One2many('estate.property.offer','property_type_id')

    offer_count = fields.Integer(string="Offer Count",compute='_compute_offer_count')

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)







