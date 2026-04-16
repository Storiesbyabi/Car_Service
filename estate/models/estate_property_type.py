from odoo import fields,models

class EstatePropertyModel(models.Model):
    _name= 'estate.property.type'
    _description = 'The Property type for estate'
    _rec_name = 'property_type'
    _unique_property_name = models.Constraint('unique(property_type)','Its must be unique')


    property_type=fields.Char()


