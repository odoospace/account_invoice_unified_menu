# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Unified Menu",

    'summary': """
        Create a new menuitem to show:
        - sale & sale refunds in the same list
        - purchase & purchase refunds in the same list
        """,

    'description': """
        Create a new menuitem to show:
        - sale & sale refunds in the same list
        - purchase & purchase refunds in the same list
    """,

    'author': "Impulzia",
    'website': "http://www.impulzia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '8.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
