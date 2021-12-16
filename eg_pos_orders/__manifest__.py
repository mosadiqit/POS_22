{
    'name': 'POS Orders Shows',
    'version': '12.0.1.0.0',
    'category': 'Point of Sale',
    'summery': 'POS Orders Shows',
    'author': '',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_view.xml',
        'views/pos_template.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'css': ['static/src/css/pos.css'],
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
