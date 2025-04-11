from odoo import models, fields

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of the properties"
    
    name = fields.Char(string = "Name", required = True)
    