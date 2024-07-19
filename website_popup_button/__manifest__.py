{
    'name': 'Web site popup button',
    'version': '1.0',
    'summary': 'Managing the website popup buttons ',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['website','sale'],
    'data': [

        'views/pop_up_button.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_popup_button/static/src/js/popup_button.js',
        ],
    },

    'installable': True,
    'auto_install': False,
}
