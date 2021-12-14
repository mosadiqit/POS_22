# -*- coding: utf-8 -*-
{
    'name': "POS Hide New Order and Delete Order",

    'summary': """
        POS Hide New Order and Delete Order
        """,

    'description': """
        POS Hide New Order and Delete Order
    """,

    'author': "da Ti Soft Consulting",
    'website': "https://www.github.com/trinanda",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '13.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml'
    ],
    'application': False,
    'installable': True,
}
