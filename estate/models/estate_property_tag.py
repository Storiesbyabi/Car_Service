from odoo import fields,models

class EstatePropertyTags(models.Model):
    _name= 'estate.property.tags'
    _rec_name ='name'

    name= fields.Char()