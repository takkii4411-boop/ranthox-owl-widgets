{
    'name': 'Sale Order Photo Capture',
    'version': '19.0.1.0.0',
    'summary': 'Capture photograph on sale orders using ranthox_image_capture',
    'category': 'Sales',
    'author': 'Ranthox Pty Ltd',
    'website': 'https://ranthox.odoo.com',
    'depends': ['sale', 'ranthox_image_capture'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
