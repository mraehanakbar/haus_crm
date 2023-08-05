{
    'name': 'Haus CRM',
    'version': '1.0',
    'summary': 'Haus CRM',
    'sequence': -9,
    'description': """Haus Customer Relationship Management""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'board',
        'dev_employee_master_data',

    ],
    'data': [
        'security/ir.model.access.csv',
        'data/cron_email.xml',
        'data/cron_category.xml',
        'views/category.xml',
        'views/log.xml',
        'views/questionare_admin.xml',
        'views/questionare_user.xml',
        'wizard/views/download_questionare.xml',
        'views/issue.xml',
        'views/menu.xml',
    ],
    'js': [
        'static/src/js/coordinates.js',  # Add this line to include your JavaScript file
    ],
    'assets': {
        'web.assets_backend': [
            'dev_crm_haus/static/**/*',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
