{
    'name': 'Web site form',
    'version': '1.0',
    'summary': 'Managing the form renddereing',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['website'],
    'data': [
        "security/ir.model.access.csv",
        'views/form_views_controllers_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_form_render/static/src/js/public_widget_form.js',
        ],
    },

    'installable': True,
    'auto_install': False,
}
