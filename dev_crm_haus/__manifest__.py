{
    'name' : 'Haus CRM',
    'version' : '1.0',
    'summary':'Haus CRM',
    'sequence':-999,
    'description':"""Haus Customer Relationship Management""",
    'category':'Productivity',
    'website':'',
    'license': 'LGPL-3',
    'depends':[
        'sale',
        'mail',
        'website_slides',
        'board'

    ],
    'data':[
        'views/category.xml',
        'views/issue.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False,
}
