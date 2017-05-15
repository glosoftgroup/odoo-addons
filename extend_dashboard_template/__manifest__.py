# -*- coding: utf-8 -*-
{
    'name': "extend_dashboard_template",

    'summary': """
        Extend Main dashboard""",

    'description': """
       Add new widgets in the main dashboard
    """,

    'author': "Glosoft group",
    'website': "http://www.glosoftgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Dashboard',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}