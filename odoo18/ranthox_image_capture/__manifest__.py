{
    'name': 'Ranthox Image Capture',
    'version': '18.0.1.0.0',
    'summary': 'Reusable camera/photograph capture OWL field widget for binary image fields',
    'category': 'Technical',
    'author': 'Ranthox Pty Ltd',
    'website': 'https://ranthox.odoo.com',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'ranthox_image_capture/static/src/xml/camera_capture.xml',
            'ranthox_image_capture/static/src/js/camera_capture.js',
            'ranthox_image_capture/static/src/xml/ranthox_image_capture.xml',
            'ranthox_image_capture/static/src/js/ranthox_image_capture.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
