# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sky Theme',
    'summary': 'Support for  themes sky in master',
    'description': 'This theme module is exclusively for master to keep the support of themes sky which were previously part of the website module in 8.0.',
    'category': 'Theme',
    'sequence': 900,
    'version': '1.0',
    'depends': ['website', 'website_sale'],
    'data': [
        'data/theme_bootswatch_data.xml',
        'views/theme_bootswatch_templates.xml','views/layout.xml','views/pages.xml',
        'views/assets.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],
    'images': ['static/description/bootswatch.png'],
    'application': True,
}
