

from odoo import fields, models,api
from datetime import timedelta
from odoo.tools.float_utils import float_is_zero,float_compare

from odoo.exceptions import UserError, ValidationError
from odoo.orm.decorators import readonly


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = ('The property for Estate')

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date( default=lambda self: fields.Date.today() + timedelta(days=90)  ,copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )

    active = fields.Boolean(default=False)
    state= fields.Selection(
        string='Status',
        selection=[
            ('new','New'),
            ('offer','Offer'),
            ('received','Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')

        ],
        default='new'
    )

    property_type_id = fields.Many2one(comodel_name="estate.property.type")

    salesman= fields.Many2one(comodel_name="res.users",default= lambda self: self.env.user )
    buyer = fields.Many2one(comodel_name="res.partner",copy=False)

    property_tags_ids= fields.Many2many(comodel_name="estate.property.tags",required=True)
    property_offers_ids = fields.One2many('estate.property.offer','property_id')

    total = fields.Float(compute='_compute_total')





    @api.depends("living_area","garden_area")
    def _compute_total(self):
        for record in self:
            record.total= record.living_area + record.garden_area

    best_offer = fields.Float(compute='_compute_best_offer')
    def _compute_best_offer(self):
        for record in self:
            pricelist = record.property_offers_ids.mapped('price')
            if len(pricelist)==0:
                record.best_offer=0
            else:
                record.best_offer=max(pricelist)


    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation='north'
        else:
            self.garden_area = 0
            self.garden_orientation= False

    def action_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError("Its sold cant cancelled")
            else:
                record.state='sold'

    def action_cancelled(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Its already Sold")
            else:
                record.state = 'cancelled'

    # Constrains
    @api.constrains('expected_price','selling_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price and record.selling_price and record.best_offer < 1:
                raise ValidationError("The price should be positive")

    @api.constrains('expected_price','selling_price')
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price,precision_digits=2):
                continue

            if float_compare(record.property_offers_ids.price,record.expected_price * 0.9,precision_digits=2) < 0:
                print(record.expected_price * 0.9)
                print(record.property_offers_ids.price)
                raise ValidationError("The price should be above 90%")
