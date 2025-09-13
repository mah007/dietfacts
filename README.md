# DietFacts - Odoo 18.0 Module

## Overview
DietFacts is an Odoo module that adds nutrition information to products. This module allows you to track calories, serving sizes, and detailed nutrient information for your products, as well as manage user meals and calculate nutrition scores.

## Features
- **Product Nutrition Information**: Add calories, serving size, and last updated date to products
- **Nutrient Management**: Define custom nutrients with units of measure and descriptions
- **Product Nutrient Details**: Associate specific nutrient values with products including daily recommended values
- **Meal Tracking**: Create and manage user meals with multiple meal items
- **Calorie Calculation**: Automatic calculation of total meal calories based on servings
- **Nutrition Scoring**: Automatic calculation of nutrition scores based on nutrient content
- **Reporting**: Generate nutrition reports for products

## Models
- `product.template` (extended): Adds nutrition fields to existing product template
- `res.users.meal`: User meal tracking
- `res.users.mealitem`: Individual items within a meal
- `product.nutrient`: Master list of nutrients
- `product.template.nutrient`: Nutrient values for specific products

## Installation
1. Copy the module to your Odoo addons directory
2. Update the app list in Odoo
3. Install the "DietFacts" module

## Odoo 18.0 Compatibility
This module has been updated for Odoo 18.0 compatibility with the following changes:
- Updated manifest file from `__openerp__.py` to `__manifest__.py`
- Changed imports from `openerp` to `odoo`
- Updated XML views: `<tree>` tags changed to `<list>` tags
- Removed deprecated `@api.one` decorators
- Updated compute methods to use record iteration
- Fixed Python 3 compatibility in import scripts
- Updated root XML element from `<openerp>` to `<odoo>`

## Usage
After installation, you'll find new menu items under Sales:
- **Diet Items**: Manage products with nutrition information
- **Meals**: Track user meals and calculate calories
- **Nutrients**: Define available nutrients

## Import Script
The module includes `importproducts.py` for bulk importing product nutrition data from CSV files. The script has been updated for Python 3 compatibility.

## Author
Greg Moss, OdooClass.com

## License
LGPL-3

## Version
18.0.1.0.0

