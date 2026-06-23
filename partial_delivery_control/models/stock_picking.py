from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state=fields.Selection(selection_add=[
        ('not_approval', 'Waiting for approval'),('done',)
    ])

    approve_flag = fields.Boolean()



    def button_validate(self):
        for rec in self.move_ids:
            if not rec.product_id.allow_partial_delivery:
                if rec.product_uom_qty != rec.quantity:
                    print('pd', rec.product_uom_qty)
                    print('pd', rec.quantity)
                return self._action_generate_backorder_wizard()
            else:
                return super().button_validate()


    def action_approve_req(self):
        return super().button_validate()




