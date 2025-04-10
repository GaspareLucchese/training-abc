{
    'name': 'Real Estate',
    'summary': 'funziona dai',
    'version': '18.0.0.0.1',
    'description': 'questo è il modulo dai',
    'license': 'OEEL-1',
    'author': 'Gaspare',
    'depends': ['crm'],
    'data': [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menu.xml",
        #data/res.country.state.csv',
        ],
    'application': True,
    'installable': True,
}