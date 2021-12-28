# Copyright 2019 Zero for information systems(https://www.erpzero.com).

{
    'name': 'Shop Logo and Delevery Reciept',
    'version': '12.0.1',
    'summary': """Logo For Each Point of Sale (Delevery Receipt & Order Receipt)""",
    'description': """This module helps you to set a logo for each point of sale.You can also see this logo in pos screen and pos receipt with special logo for each pos header+footer and customer address + mobile + phone + Vat""",
    'category': 'Point Of Sale',
    'author': 'Zero Systems,cybrosys',
    'company': 'Zero for Information Systems',
    'website': "https://www.erpzero.com",
    'email': "sales@erpzero.com",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config_image_view.xml',
        'views/pos_image_view.xml',
    ],
    'qweb': [],
    'images': ['static/description/logo.PNG'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
