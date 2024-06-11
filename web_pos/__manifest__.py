{
    'name': 'JavaScript Practice',
    'version': '1.0',
    'summary': 'JavaScript Practice Module',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['base', 'web', 'hr_expense', 'purchase','website','web_enterprise', 'website_enterprise','planning'],
    'data': ['data/hr_mail.xml', 'views/res_list_views.xml'],
    'assets': {
        'web.assets_backend': ['web_pos/static/src/js/res_partner_views.js',
                                # 'web_pos/static/src/js/planing_custom_button.js',
                               'web_pos/static/src/xml/res_partner_list_view.xml',

        ],
        'web.assets_frontend': [
            'web_pos/static/src/js/public_widget.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
