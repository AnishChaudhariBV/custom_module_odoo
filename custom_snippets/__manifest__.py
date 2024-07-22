{
    'name': 'Web site Custom Snnipets',
    'version': '1.0',
    'summary': 'create the custom snipets ',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['website','web_editor','sale'],
    'data': [

        'views/testing_snippets.xml',
        'views/age_calculator_snippets.xml',
        'views/search_sale_order_snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_snippets/static/src/js/age_calculator_snippets.js',
            'custom_snippets/static/src/js/search_sale_order.js',
        ],
    },

    'installable': True,
    'auto_install': False,
}
