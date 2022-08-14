# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Multi Language Stock Translation',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Multi Language Stock Translation',
    'author': 'FF',
    'description': """

""",
    'depends': ['base', 'stock'],
    'data': [
        'views/res_company_views.xml',
        'views/res_config_setting_views.xml',
    ],
    'demo': [''],
    'qweb': [''],
    'installable': True,
    'auto_install': False,
}
