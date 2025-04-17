from odoo import fields, models

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _inherit = "estate.mixin"
    _description = "Tag to assign to a property"
    _order = "name"
    _sql_constraints = [
        ("unique_tag_name","UNIQUE(name)","Tag name should be unique")
    ]
    
    color = fields.Integer()
    
    