{
    'name': 'practice',
    'version': '1.0',
    'summary': 'this is practice module',
    'description': 'for practice purpose',
    'category': 'practice',
    'author': 'Anish',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/practice_view.xml',
        'views/practice_1_views.xml',
        # 'views/contrl.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False,

}