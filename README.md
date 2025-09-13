# DietFacts - Odoo 18.0 Module

## Overview
DietFacts is a comprehensive Odoo module that adds nutrition information management to products. This module allows you to track calories, serving sizes, detailed nutrient information, manage user meals, and calculate nutrition scores. Perfect for food industry, restaurants, and health-conscious businesses.

## Features
- **Product Nutrition Information**: Add calories, serving size, and last updated date to products
- **Nutrient Management**: Define custom nutrients with units of measure and descriptions
- **Product Nutrient Details**: Associate specific nutrient values with products including daily recommended values
- **Meal Tracking**: Create and manage user meals with multiple meal items
- **Calorie Calculation**: Automatic calculation of total meal calories based on servings
- **Nutrition Scoring**: Automatic calculation of nutrition scores based on nutrient content (e.g., sodium levels)
- **Reporting**: Generate nutrition reports for products
- **Data Import**: Bulk import nutrition data from CSV files

## Models
- `product.template` (extended): Adds nutrition fields to existing product template
- `res.users.meal`: User meal tracking with automatic calorie calculation
- `res.users.mealitem`: Individual items within a meal
- `product.nutrient`: Master list of nutrients with UOM support
- `product.template.nutrient`: Nutrient values for specific products

## Installation
1. Copy the module to your Odoo addons directory
2. Update the app list in Odoo
3. Install the "DietFacts" module

## Usage
After installation, you'll find new menu items under Sales:
- **Diet Items**: Manage products with nutrition information
- **Meals**: Track user meals and calculate calories
- **Nutrients**: Define available nutrients

## Odoo 18.0 Compatibility Updates

### Major Improvements Made:
1. **Enhanced Manifest Structure**:
   - Added proper UOM module dependency
   - Improved category structure (`Sales/Sales`)
   - Enhanced description with detailed feature list
   - Added proper website and demo fields

2. **Modernized Python Code**:
   - Updated class names to follow Odoo 18.0 conventions (CamelCase)
   - Added comprehensive field descriptions and help text
   - Improved model definitions with proper defaults
   - Enhanced field relationships with `ondelete` attributes
   - Added `_description` and `_order` attributes to models

3. **Updated XML Views**:
   - Changed all `<tree>` tags to `<list>` tags (critical Odoo 18.0 requirement)
   - Removed deprecated `view_type` attributes from actions
   - Updated CSS classes (`o_view_nocontent_smiling_face` instead of `oe_view_nocontent_create`)
   - Changed view modes from `tree` to `list`
   - Added proper form and list views for nutrient management

4. **Enhanced Security**:
   - Updated access rights for better usability
   - Proper CRUD permissions for all models
   - Maintained security while improving user experience

5. **Code Quality Improvements**:
   - Better field organization and documentation
   - Improved compute method implementations
   - Enhanced user experience with better defaults
   - Modern Odoo development practices

### Breaking Changes Addressed:
- ✅ List view XML tags: `<tree>` → `<list>` (HIGH impact)
- ✅ Removed deprecated `@api.one` decorators
- ✅ Updated imports from `openerp` to `odoo`
- ✅ Modernized XML structure and attributes
- ✅ Enhanced UOM module integration

## Import Script
The module includes `importproducts.py` for bulk importing product nutrition data from CSV files. The script has been updated for Python 3 compatibility with proper error handling.

## Technical Details
- **Dependencies**: `sale`, `uom`
- **Odoo Version**: 18.0+
- **License**: LGPL-3
- **Author**: Greg Moss, OdooClass.com
- **Website**: https://odooclass.com

## Version History
- **18.0.1.0.0**: Major update for Odoo 18.0 compatibility with enhanced features and modern code structure

## Support
For issues, feature requests, or contributions, please visit the GitHub repository.

