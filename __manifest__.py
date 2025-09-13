{
    'name': 'DietFacts',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Adds nutrition information to products',
    'description': """
DietFacts - Product Nutrition Information
=========================================

This module extends Odoo's product management with comprehensive nutrition tracking capabilities:

* Add calories, serving size, and nutrition scores to products
* Define custom nutrients with units of measure
* Track detailed nutrient values per product
* Manage user meals and calculate total calories
* Generate nutrition reports for products
* Import nutrition data from CSV files

Perfect for food industry, restaurants, and health-conscious businesses.
    """,
    'author': 'Greg Moss, OdooClass.com',
    'website': 'https://odooclass.com',
    'license': 'LGPL-3',
    'depends': ['sale', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'dietfacts_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

