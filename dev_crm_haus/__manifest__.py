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
        'security/security.xml',
        'views/category.xml',
        'views/issue.xml',
        'views/menu.xml',
        'static/js/geolocation.js'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
