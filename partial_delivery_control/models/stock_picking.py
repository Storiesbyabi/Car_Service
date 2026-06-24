

from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state=fields.Selection(selection_add=[
        ('not_approval', 'Waiting for approval'),('done',)
    ])

    approve_flag = fields.Boolean(default=True)



    def _action_generate_backorder_wizard(self, show_transfers=False):
        for rec in self.move_ids:
            if not rec.product_id.allow_partial_delivery and self.approve_flag == True:
                print('in', self.approve_flag)
                if rec.product_uom_qty != rec.quantity:
                    print('pd', rec.product_uom_qty)
                    print('pd', rec.quantity)
                return super(StockPicking, self.with_context(hide_button=False))._action_generate_backorder_wizard(show_transfers=False)

            else:
                self.approve_flag = False
                print('out', self.approve_flag)
                return super(StockPicking, self.with_context(hide_button=True))._action_generate_backorder_wizard(show_transfers=False)

    def button_validate(self):
        if self.state == 'assigned':
            self.approve_flag = True
        else:
            self.approve_flag = False
        print('flag',self.approve_flag)
        return super().button_validate()





