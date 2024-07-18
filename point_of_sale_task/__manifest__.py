{
    'name': 'Point Of sale Practice',
    'version': '1.0',
    'summary': 'point of sale Practice Module',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': [
        'base', 'web', 'purchase', 'website', 'point_of_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_views.xml',
        'views/pos_seeting_views.xml',
        'views/pos_config_views.xml',
        "views/location_views.xml",
        "views/cutom_views.xml",

    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'point_of_sale_task/static/src/js/pos_custom_note_button.js',
            'point_of_sale_task/static/src/xml/pos_custom_button_view.xml',
            'point_of_sale_task/static/src/xml/payment_button_view.xml',
            'point_of_sale_task/static/src/js/payment_screen_button.js',
            'point_of_sale_task/static/src/js/pos_product_clear_button.js',
            'point_of_sale_task/static/src/xml/pos_product_clear_button.xml',
            'point_of_sale_task/static/src/custom.scss',
            'point_of_sale_task/static/src/js/total_item_count_pos.js',
            'point_of_sale_task/static/src/js/pos_discount_button.js',
            'point_of_sale_task/views/pos_views.xml',
            'point_of_sale_task/static/src/js/add_note_pos.js',
            'point_of_sale_task/static/src/xml/cutomer_inherit_button.xml',
            'point_of_sale_task/static/src/js/customer.js',
            'point_of_sale_task/static/src/js/pos_location_button.js',
            'point_of_sale_task/static/src/xml/pos_location.xml',
            'point_of_sale_task/static/src/xml/location_screen_tenplate.xml',
            'point_of_sale_task/static/src/js/add_location_screen.js',
            'point_of_sale_task/static/src/xml/location_receipit.xml',
            'point_of_sale_task/static/src/js/Custom_contact.js',
            'point_of_sale_task/static/src/xml/custom_contact.xml',
            'point_of_sale_task/static/src/js/customer_screen.js',
            'point_of_sale_task/static/src/xml/customer_screen.xml',


        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}