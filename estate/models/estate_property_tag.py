from odoo import fields,models

class EstatePropertyTags(models.Model):
    _name= 'estate.property.tags'
    _rec_name ='name'

    # Not working 

    _unique_property_tag = models.Constraint('unique(name)', 'Its must be unique')

    name = fields.Char()