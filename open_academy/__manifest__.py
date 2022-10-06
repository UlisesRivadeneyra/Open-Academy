{
    'name': "OpenAcademy",
    'license': "LGPL-3",
    'summary': """This is the open academy course of Vauxoo""",
    'author': "Vauxoo",
    'website': "http://www.yourcompany.com",
    'installable': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/open_academy_course_views.xml',
        'views/open_academy_session_views.xml',
        'views/res_partner_views.xml',
        'views/open_academy_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/open_academy_demo.xml',
        'demo/res_partner_category_demo.xml',
    ],
}
