from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

ECHARTS_TYPE = [
    ('Calendar', 'Calendar'),  # 日历图
    ('Funnel', 'Funnel'),  # 漏斗图
    ('Graph', 'Graph'),  # 关系图
    ('Liquid', 'Liquid'),  # 水球图
    ('Parallel', 'Parallel'),  # 平行坐标图
    ('Pie', 'Pie'),  # 饼图
    ('Polar', 'Polar'),  # 极坐标系
    ('Rader', 'Rader'),  # 雷达图
    ('Sankey', 'Sankey'),  # 桑基图
    ('Sunburst', 'Sunburst'),  # 旭日图
    ('ThemeRiver', 'ThemeRiver'),  # 主题河流图
    ('WordCloud', 'WordCloud'),  # 词云图
]  # 目前先处理基本图表


class EchartsType(models.Model):
    _name = 'echarts.type'
    _description = 'Echarts Type'

    name = fields.Char(string='Name')
    etype = fields.Char(string='Etype')
    is_toolbox = fields.Boolean(string='Display ToolboxOpts')
    is_title = fields.Boolean(string='Display TitleOpts')
    title = fields.Char(string='TitleOpts')
    is_subtitle = fields.Boolean(string='Display SubTitle')
    subtitle = fields.Char(string='SubTitle')
