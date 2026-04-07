from odoo import fields,models


class CarPurchase(models.Model):
    _inherit = 'purchase.order'
