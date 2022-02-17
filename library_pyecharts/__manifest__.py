# -*- coding: utf-8 -*-
{
    'name': 'Odoo Dashboard Library pyecharts',
    'version': '15.0.0.1',
    'category': 'Tools',
    'description': '',
    'author': 'Library pyecharts',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'data/echarts_type_data.xml',
        'data/dashboard_data.xml',
        # 'views/assets_backend.xml',
        'views/home.xml',
        'views/echarts_type_view.xml',
        'views/dashboard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'library_pyecharts/static/src/js/echarts.min.js',
            'library_pyecharts/static/src/js/china.js',
            'library_pyecharts/static/src/js/load_pyecharts.js',
            'library_pyecharts/static/src/css/adminlte.min.css',
            'library_pyecharts/static/src/js/theme_dark.js',
            'library_pyecharts/static/src/js/theme_macarons.js',
            'library_pyecharts/static/src/js/theme_vintage.js',
            'library_pyecharts/static/src/js/theme_infographic.js',
            'library_pyecharts/static/src/js/theme_roma.js',
            'library_pyecharts/static/src/js/theme_shine.js',
        ],
        'web.assets_qweb': [
            'library_pyecharts/static/src/xml/**/*',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
}
