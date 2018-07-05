# -*- coding: utf-8 -*-
{
    'name': "Report expenses from website",

    'summary': 
        """
            * Create expenses form website with a portal user. \n
            * A expense can be related to a project.
        """,

    'description':
        """
            A employee has a portal user, this user can report expenses it is related to a project.
        """,

    'author': "Soluciones4G - OGM",
    'website': "",
    'license': 'AGPL-3',

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'web',
        'website_form',
        'hr',
        'project'
    ],

    'demo': [],

    'data': [
        'views/expense_inherit_view.xml',
        'views/project_inherit_view.xml',
        'views/portal_templates.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
