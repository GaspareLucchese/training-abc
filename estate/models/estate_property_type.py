from odoo import models, fields

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "testiamo"
    
    name = fields.Char(string = "Name", required = True)
    