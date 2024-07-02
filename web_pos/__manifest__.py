{
    'name': 'JavaScript Practice',
    'version': '1.0',
    'summary': 'JavaScript Practice Module',
    'author': 'Anish Chaudhari',
    'sequence': -10,
    'depends': [
        'base', 'web', 'hr_expense', 'purchase', 'website',
        'planning', 'sale', 'stock', 'point_of_sale'
    ],
    'data': [
        'data/hr_mail.xml',
        'views/res_list_views.xml',
        'views/stock_picking_js_connection.xml',
        'views/pos_views.xml',
        'views/pos_seeting_views.xml'


    ],
    'assets': {
        'web.assets_backend': [
            'web_pos/static/src/js/res_partner_views.js',
            # 'web_pos/static/src/js/planing_custom_button.js',
            'web_pos/static/src/xml/res_partner_list_view.xml',
            'web_pos/static/src/controller/custom_button_stock_picking.js',
        ],
        'point_of_sale._assets_pos': [
            'web_pos/static/src/js/pos_custom_button.js',
            'web_pos/static/src/xml/pos_custom_button_view.xml',
            'web_pos/static/src/xml/payment_button_view.xml',
            'web_pos/static/src/js/payment_screen_button.js',
            'web_pos/static/src/js/pos_product_clear_button.js',
            'web_pos/static/src/xml/pos_product_clear_button.xml',
            'web_pos/static/src/custom.scss',
            'web_pos/static/src/js/total_item_count_pos.js',
            'web_pos/static/src/js/pos_discount_button.js',
            'web_pos/views/pos_views.xml',
            'web_pos/static/src/js/add_note_pos.js',
            # 'web_pos/static/src/js/reciept_custom.js',
            # 'web_pos/static/src/xml/reciept_views.xml',
            # 'web_pos/static/src/js/customer.js'
            'web_pos/static/src/xml/cutomer_inherit_button.xml',
            'web_pos/static/src/js/customer.js'

        ],
        'web.assets_frontend': [
            'web_pos/static/src/js/public_widget.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
