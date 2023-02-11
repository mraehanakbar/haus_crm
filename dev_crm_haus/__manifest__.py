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

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/category.xml',
        'views/issue.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
