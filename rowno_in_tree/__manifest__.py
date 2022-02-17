# -*- encoding: utf-8 -*-
{
    'name': "Row Number in tree/list view",
    'version': '15.0.0',
    'summary': 'Show row number in tree/list view.',
    'category': 'Other',
    'description': """By installing this module, user can see row number in Odoo backend tree view.""",
    "depends" : ['web'],
    'data': [
             'views/listview_templates.xml',
             ],
    'qweb': [
           'static/src/xml/base.xml',
            ],

    'images': ['static/description/rowno_tree-banner.png'],
            
    # Author
    'author': 'Synodica Solutions Pvt. Ltd.',
    'website': 'https://synodica.com',
    'maintainer': 'Synodica Solutions Pvt. Ltd.',
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
