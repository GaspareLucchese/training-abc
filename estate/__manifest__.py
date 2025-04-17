{
    'name': 'Real Estate',
    'summary': 'Sell house easily',
    'version': '18.0.0.0.1',
    'description': 'Module created as technical training for Odoo 18',
    'license': 'OEEL-1',
    'author': 'Gaspare',
    'depends': ['base', 'mail'],
    'data': [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menu.xml",
        ],
    'application': True,
    'installable': True,
}