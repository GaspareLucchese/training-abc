from odoo import models, fields, api, _

class PropertyType(models.Model):
    _name = "estate.property.type"
    _inherit = "estate.mixin"
    _description = "Types of the properties"
    _order = "sequence desc"
    _sql_constraints = [
        ("unique_type_name","UNIQUE(name)","Type name should be unique")
    ]
    
    sequence = fields.Integer(default = 1)
    property_count = fields.Integer(compute="_compute_property_count")
    offer_count = fields.Integer(compute="_compute_offer_count")
    
    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    
    #Riv struttura
    def action_open_property_ids(self):
        return {
            "name": _("Related Properties"),
            "type": "ir.actions.act_window",
            "view_mode": "list,form",
            "res_model": "estate.property",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id}
        }
        
    def action_open_offer_ids(self):
        return {
            "name": _("Related Offers"),
            "type": "ir.actions.act_window",
            "view_mode": "list,form",
            "res_model": "estate.property.offer",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id}
        }
        
    
    @api.depends("property_ids")
    def _compute_property_count(self):
        for rec in self:
            rec.property_count = len(rec.property_ids)
            
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)
    
    #ogni volta che creiamo un type, creiamo anche un tag        
    @api.model
    def create(self ,vals_list):
        if "name" in vals_list:
            self.env["estate.property.tag"].create(
                {
                    "name" : vals_list.get("name")
                }
            )
        return super().create(vals_list)
    
    #ogni volta che eliminiamo un type cancelliamo tutte le proprietà relative a quel type
    def unlink(self):
        self.property_ids.state = "cancelled"
        return super().unlink()