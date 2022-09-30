# -*- coding: utf-8 -*-
{
    'name': "OpenAcademy",
    'license': "LGPL-3",
    'summary': """
        This is the open academy course of Vauxoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ulises",
    'website': "http://www.yourcompany.com",
    'installable': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'views/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/course_views.xml',
        'views/course_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/course_demo.xml'
    ],
}
