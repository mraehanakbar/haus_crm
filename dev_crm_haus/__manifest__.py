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
        'board',
        'dev_employee_master_data',

    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/issue.xml',
        'views/category.xml',
        'views/log.xml',
        'views/questionare_admin.xml',
        'views/questionare_user.xml',
        'wizard/views/download_report_questionare.xml',
        'views/menu.xml',
    ],

    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
