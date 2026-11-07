{
    'name': 'Ranthox X2Many Search Bar',
    'version': '17.0.1.0.0',
    'summary': 'Adds a live search bar above any One2many or Many2many list in form views',
    'category': 'Technical',
    'author': 'ranthox17',
    'website': 'https://www.ranthox.com',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'ranthox_x2many_search/static/src/xml/searchable_x2many.xml',
            'ranthox_x2many_search/static/src/js/searchable_x2many.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
