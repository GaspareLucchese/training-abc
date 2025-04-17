from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

class EstateProperty(models.Model):
    
    _name = "estate.property"
    _description = "Property to sell/buy"
    _order = "id desc"
    _sql_constraints = [
        ("positive_expected_price","CHECK(expected_price > 0)","The expected price should be positive"),
        ("positive_selling_price","CHECK(selling_price > 0)","The selling price should be positive")
    ]
    
    active = fields.Boolean(default=True)
    name = fields.Char(
        default = "Unknown", 
        required = True
    )
    description = fields.Text()
    state = fields.Selection(
        [
            ('new', 'New'),
            ('received', 'Offer Received'),
            ('accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        required = True,
        copy = False,
        default = "new"
    )
    postcode = fields.Char()
    
    #non si capisce la consegna dei 3 mesi (Esercizio 5)
    def _default_date(self):
        return fields.Date.today()
    date_availability = fields.Date(default = _default_date)
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        #string="Type",
        selection=[
            ('north', 'North'),
            ('est', 'Est'),
            ('south', 'South'),
            ('west', 'West'),
        ]  
    )
    last_seen = fields.Datetime("Last Seen", default = fields.Datetime.now)
    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")

    salesman_id = fields.Many2one("res.users", string = "Salesman", required=True)
    buyer_id = fields.Many2one("res.partner", string = "Buyer")
    property_type_id = fields.Many2one("estate.property.type", string = "Property Type")
    offer_ids = fields.One2many("estate.property.offer","property_id",string = "Offerte")
    tag_ids = fields.Many2many("estate.property.tag", string = "Tags")
    
    @api.depends("living_area", "garden_area")
    def _compute_total_area (self):
        for rec in self:
            rec.total_area = rec.garden_area + rec.living_area
    
    @api.depends("offer_ids.price")        
    def _compute_best_offer(self):
        for rec in self:
            rec.best_offer = max(rec.offer_ids.mapped('price'), default=0.0)
            
    @api.onchange("garden")
    def _onchange_garden(self):
        for rec in self:
            if rec.garden == False:
                rec.garden_area = 0
                
    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        for rec in self:
            if (rec.date_availability - fields.Date.today()).days < 0:
                return {
                    "warning":
                        {
                            "title": _("Warning"),
                            "message": _("The date is in the past, set a date after today")
                        }
                }
                
    def action_sell(self):
        if self.state == "sold":
            raise UserError(_("The property result alredy sold"))
        self.state = "sold"
        #aggiungere un compratore e un venditore
        
    def action_cancel(self):
        if self.state == "sold" or self.state == "accepted":
            raise UserError(_("The property result alredy sold"))
        else:
            self.state = "cancelled"
    
    @api.constrains("selling_price")        
    def _check_constraint(self):
        for estate in self:
            if estate.selling_price < 5000:
                raise ValidationError(_("The selling price is too low"))
            
            
    def unlink(self):
        if self.state == 'cancelled' or self.state == 'new':
            return super().unlink()
        else:
            raise UserError(_("It's not possible to delete this property"))