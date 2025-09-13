# DietFacts application
from odoo import models, fields, api

# Extend product.template model with nutrition information

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories", help="Calories per serving")
    servingsize = fields.Float('Serving Size', help="Standard serving size")
    lastupdated = fields.Date('Last Updated', help="Date when nutrition information was last updated")
    nutrient_ids = fields.One2many('product.template.nutrient', 'product_id', 'Nutrients')
    
    @api.depends('nutrient_ids', 'nutrient_ids.value')
    def _calcscore(self):
        for record in self:
            currentscore = 0
            for nutrient in record.nutrient_ids:
                if nutrient.nutrient_id.name == 'Sodium':
                    currentscore = currentscore + (nutrient.value / 5)
            record.nutrition_score = currentscore
    nutrition_score = fields.Float(string="Nutrition Score", store=True, compute="_calcscore", help="Calculated nutrition score based on nutrients")
    
class ResUsersMeal(models.Model):
    _name = 'res.users.meal'
    _description = 'User Meal'
    _order = 'meal_date desc'
    
    name = fields.Char("Meal Name", required=True)
    meal_date = fields.Datetime("Meal Date", default=fields.Datetime.now)
    item_ids = fields.One2many('res.users.mealitem', 'meal_id', 'Meal Items')
    user_id = fields.Many2one('res.users', 'Meal User', default=lambda self: self.env.user)
    largemeal = fields.Boolean("Large Meal", help="Automatically set when meal exceeds 500 calories")
    
    @api.onchange('totalcalories')
    def check_totalcalories(self):
        if self.totalcalories > 500:
            self.largemeal = True
        else:
            self.largemeal = False
             
    @api.depends('item_ids', 'item_ids.servings')
    def _calccalories(self):
        for record in self:
            currentcalories = 0
            for mealitem in record.item_ids:
                currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
            record.totalcalories = currentcalories
       
    totalcalories = fields.Integer(string="Total Meal Calories", store=True, compute="_calccalories")
    notes = fields.Text('Meal Notes')
    
class ResUsersMealItem(models.Model):
    _name = 'res.users.mealitem'
    _description = 'Meal Item'
    
    meal_id = fields.Many2one('res.users.meal', 'Meal', ondelete='cascade')
    item_id = fields.Many2one('product.template', 'Meal Item', required=True)
    servings = fields.Float('Servings', default=1.0)
    calories = fields.Integer(related='item_id.calories', string="Calories Per Serving", store=True, readonly=True)
    notes = fields.Text("Meal item notes")

class ProductNutrient(models.Model):
    _name = 'product.nutrient'
    _description = 'Product Nutrient'
    
    name = fields.Char("Nutrient Name", required=True)
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure')
    description = fields.Text("Description")
    
class ProductTemplateNutrient(models.Model):
    _name = 'product.template.nutrient'
    _description = 'Product Template Nutrient'
    
    nutrient_id = fields.Many2one('product.nutrient', string="Product Nutrient", required=True)
    product_id = fields.Many2one('product.template', 'Product', ondelete='cascade')
    uom = fields.Char(related='nutrient_id.uom_id.name', string="UOM", readonly=True)
    value = fields.Float('Nutrient Value')
    dailypercent = fields.Float("Daily Recommended Value (%)")
    
    

    
    
    