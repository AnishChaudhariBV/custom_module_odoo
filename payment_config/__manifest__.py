{
    'name': 'Payment CyberSource',
    'version': '1.0',
    'depends': ['payment','sale'],
    'data': [
        'views/cybersource_payement_views.xml',
        'views/sale_order_payment_buuton.xml',
        'data/cybersource_payment_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}
