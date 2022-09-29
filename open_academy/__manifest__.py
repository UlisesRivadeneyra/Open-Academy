<<<<<<< HEAD
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

=======
{
    'name': "OpenAcademy",
    'license': "LGPL-3",
    'summary': """This is the open academy course of Vauxoo""",
    'author': "Vauxoo",
    'website': "http://www.yourcompany.com",
    'installable': True,
>>>>>>> main
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
<<<<<<< HEAD
    'version': '0.1',

    # any module necessary for this one to work correctly
<<<<<<< HEAD
    'depends': ['base'],

    # always loaded
    'data': [
        #'views/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/course_views.xml',
        'views/course_menu_views.xml',
=======
    'depends': ['base', 'board'],
    # always loaded
    'data': [
        'security/security.xml',
=======
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
>>>>>>> main
        'security/ir.model.access.csv',
        'views/open_academy_course_views.xml',
        'views/open_academy_session_views.xml',
        'views/res_partner_views.xml',
<<<<<<< HEAD
        'wizard/open_academy_wizard_views.xml',
        'reports/open_academy_session_reports.xml',
        'views/open_academy_dashboard_views.xml',
        'views/open_academy_menu_views.xml',
>>>>>>> 42c5372 ( [ADD]open_academy: Added reports,wizard and i18n T#60931)
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/course_demo.xml'
=======
        'views/open_academy_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/open_academy_demo.xml',
        'demo/res_partner_category_demo.xml',
>>>>>>> main
    ],
}
