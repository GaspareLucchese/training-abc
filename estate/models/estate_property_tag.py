from odoo import fields, models

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag to assign to a property"
    
    name = fields.Char(string = "Name", required=True)