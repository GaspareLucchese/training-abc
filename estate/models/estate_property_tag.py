from odoo import fields, models

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "testiamo 3"
    
    name = fields.Char(string = "Name", required=True)