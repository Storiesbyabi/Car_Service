

from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state=fields.Selection(selection_add=[
        ('not_approval', 'Waiting for approval'),('done',)
    ])

    approve_flag = fields.Boolean(default=True)



    def validate_button(self):
        for rec in self.move_ids:
            if not rec.product_id.allow_partial_delivery and approve_flag:
                print('in', self.approve_flag)
                if rec.product_uom_qty != rec.quantity:
                    print('pd', rec.product_uom_qty)
                    print('pd', rec.quantity)
                return super(StockPicking, self.with_context(hide_button=False)).validate_button()

            else:
                self.approve_flag = True
                print('out', self.approve_flag)
                return super(StockPicking, self.with_context(hide_button=True)).validate_button()

    def action_approve_req(self):
        self.approve_flag = False
        return self.validate_button()




