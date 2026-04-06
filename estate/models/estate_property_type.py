from odoo import fields,models

class EstatePropertyModel(models.Model):
    _name= 'estate.property.type'
    _description = 'The Property type for estate'
    _rec_name = 'property_type'

    property_type=fields.Char()

