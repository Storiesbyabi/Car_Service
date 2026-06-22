from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state=fields.Selection([
        ('not_approval', 'Waiting for approval'),
    ])



    @api.onchange('state')
    def check_partial_delivery(self):
        print(234567,self)