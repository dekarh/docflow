# -*- coding: utf-8 -*-
{
    'name': "docflow",

    'summary': """
        Документооборот для flectra в стиле ПланФикс 
        """,

    'description': """
        Документооборот для flectra в стиле ПланФикс
        """,

    'author': "Денис Алексеев",
    'website': "https://github.com/dekarh/docflow",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sign',
    'version': '0.0.6',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/hr_views.xml',
        'views/docflow_views.xml',
        #'views/views.xml',
        #'views/templates.xml',
        'data/res.users.csv',
        'data/res.groups.csv',
        #'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}