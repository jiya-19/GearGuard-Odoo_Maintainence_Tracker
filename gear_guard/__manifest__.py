{
    'name': 'GearGuard',
    'version': '1.0',
    'category': 'Maintenance',
    'summary': 'Equipment & Maintenance Management System',
    'author': 'HackOps',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/maintenance_team_views.xml',
        'views/maintenance_request_views.xml',
        'views/menu.xml',
    ],
    'application': True,
}

