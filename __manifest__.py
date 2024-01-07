{
    'name' : 'Odoo Module Template',
    'version' : '1.0',
    'summary': 'Odoo Module Template',
	"author": "Odoo Data, C.A.",
	'support': 'webmaster@odoodata.com',
    'sequence': -100,
    'description': """Odoo Data Template""",
    'category': 'Templates',
    'website': 'https://odoodata.com',
	"development_status": "Beta",
	'license': 'LGPL-3',
    'depends' : ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'views/client_view.xml',
		    'menus/menu.xml',
        'reports/gym_client_card.xml',
    ],
	'images' : [],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
