from odoo import models, fields

class EstateProperty(models.Model):
    
    _name = "estate.property"
    _description = "Vorrei solo funzionasse"
    
    #rivedere a che serve active (Esercizi 5)
    active = fields.Boolean(
        default=True, 
        #non funziona l'invisible
        invisible=True)
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
    # _deafult_date è un metodo!
    def _default_date(self):
        return fields.Date.today()
    
    date_avalability = fields.Date(default = _default_date)
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

    property_type_id = fields.Many2one("estate.property.type", string = "Tipo di Proprietà")
    offer_ids = fields.One2many("estate.property.offer","property_id",string = "Offerte")
    tag_ids = fields.Many2many("estate.property.tag", string = "Tags")