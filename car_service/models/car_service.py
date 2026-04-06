from odoo import fields,models

class CarService(models.Model):
    _name='car.service'
    _description = ("The car service module")

    name=fields.Char()
