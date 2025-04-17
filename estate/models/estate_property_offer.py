from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError
#alternative?
from datetime import timedelta

class EstateOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers for the properties"
    _order = "price desc"
    _sql_constraints = [
        ("positive_offer_price","CHECK(price > 0)","The offer price should be positive")
    ]
    
    price = fields.Float()
    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy = False,
    )
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)
    
    @api.depends("validity")
    def _compute_date_deadline(self):
        for rec in self:
            rec.date_deadline = fields.Date.today() + timedelta(days=rec.validity)
            
    @api.depends("date_deadline")
    def _inverse_date_deadline(self):
        for rec in self:
            if (rec.date_deadline - fields.Date.today()).days >= 0:
                rec.validity = (rec.date_deadline - fields.Date.today()).days
                
    @api.onchange("date_deadline")
    def _onchange_date_deadline(self):
        for rec in self:
            if (rec.date_deadline - fields.Date.today()).days < 0:
                return {
                    "warning":
                        {
                            "title": ("Warning"),
                            "message": ("The date is in the past, set a date after today")
                        }
                }
    
    def action_accept(self):
        self.ensure_one() #assicura che questo metodo è richiamato da un solo record
        if "accepted"in self.property_id.offer_ids.mapped("status"):
            raise UserError(_("The offer result alredy accepted"))
        self.status = "accepted"
        self.property_id.state = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id.id
        #? aggiungere cambiamento agli stati di property
    
    def action_refuse(self):
        self.ensure_one()
        if self.status == "accepted":
            raise UserError(_("Another offer was already accepted"))
        else:
            self.status = "refused"
            

    @api.constrains("price")
    def _offer_too_low(self):
        for offer in self:
            if offer.price < (self.property_id.expected_price * 0.9):
                raise ValidationError(_("The selling price must be at least 90%"))
            
    @api.model
    def create(self, vals):
        self.env['estate.property'].browse(vals['property_id']).state = 'received'
        return super().create(vals)