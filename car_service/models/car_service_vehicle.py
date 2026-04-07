from odoo import fields,models


class CarServiceVehicle(models.Model):
    _inherit = "fleet.vehicle.log.services"


    customer_name = fields.Char()
    previous_date = fields.Date()


