{
    'name': 'Web site edit',
    'version': '1.0',
    'summary': 'Managing the edit data from the portal side',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': ['website','base'],
    'data': ['security/ir.model.access.csv',
             'views/add_menu_in_portal_views.xml',
             "views/custom_form_views.xml",
             "views/menu_views.xml",
             "views/custom_form_web_site_template.xml",


    ],
    'assets': {
        'web.assets_frontend': [
            'edit_at_portal_level_task/static/src/scss/custom_form.scss',
        ],
    },

    'installable': True,
    'auto_install': False,
}
