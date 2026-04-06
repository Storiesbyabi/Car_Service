from odoo import fields, models,api
from datetime import timedelta

from odoo.orm.decorators import readonly


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'

    price = fields.Float()
    status = fields.Selection(copy=False,
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    partner_id = fields.Many2one(comodel_name='res.partner',required=True)
    property_id = fields.Many2one(comodel_name='estate.property',required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline',inverse='_inverse_validity',store=True)


    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                createdate = record.create_date.date()
            else:
                createdate = fields.Date.today()


            record.date_deadline = timedelta(days=record.validity) + createdate

    def _inverse_validity(self):
        for record in self:
            createdate = record.create_date.date()
            delta = record.date_deadline - createdate
            record.validity = delta.days

    def action_accept(self):
        for record in self:
            record.status='accepted'
        return True
    def action_cancel(self):
        for record in self:
            record.status='refused'
        return True

    




