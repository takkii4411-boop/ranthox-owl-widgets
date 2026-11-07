{
    'name': 'Ranthox Excel Editor Widget',
    'version': '18.0.1.0.0',
    'summary': 'OWL widget to upload and view Excel files inline',
    'category': 'Hidden',
    'author': 'Ranthox Official',
    'website': 'https://ranthox.com',
    'license': 'Other proprietary',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'ranthox_excel_editor/static/lib/xlsx/xlsx.full.min.js',
            'ranthox_excel_editor/static/lib/jszip/jszip.min.js',
            'ranthox_excel_editor/static/lib/x-spreadsheet/xspreadsheet.css',
            'ranthox_excel_editor/static/lib/x-spreadsheet/xspreadsheet.js',
            'ranthox_excel_editor/static/src/xml/ranthox_excel_editor.xml',
            'ranthox_excel_editor/static/src/js/ranthox_excel_editor.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
