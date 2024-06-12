{
    'name': 'JavaScript Practice',
    'version': '1.0',
    'summary': 'JavaScript Practice Module',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['base', 'web', 'hr_expense', 'purchase', 'website', 'planning', 'sale','stock'],
    'data': ['data/hr_mail.xml', 'views/res_list_views.xml', 'views/stock_picking_js_connection.xml'],
    'assets': {
        'web.assets_backend': ['web_pos/static/src/js/res_partner_views.js',
                               # 'web_pos/static/src/js/planing_custom_button.js',
                               'web_pos/static/src/xml/res_partner_list_view.xml',
                               'web_pos/static/src/controller/custom_button_stock_picking.js',


                               ],
        'web.assets_frontend': [
            'web_pos/static/src/js/public_widget.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
