{
    'name': 'Substitute Product Management',
    'version': '1.0',
    'summary': 'managing the products in sale order' ,
    'author': 'Anish Chaudhari',
    'sequence':-10,

    'depends': ['base','sale','product'],
    'data': ['security/ir.model.access.csv',
             'views/sale_order_line.xml',
             "reports/substitude_product_report.xml",
             'views/product_template_inherit.xml',
             'wizard/substitute_product_wizard_views.xml'
             ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
