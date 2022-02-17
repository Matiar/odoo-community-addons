from odoo import http
import json
import random
from odoo.http import request
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.charts import Gauge
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker

import logging

_logger = logging.getLogger(__name__)


class Demo(http.Controller):
    @http.route('/demo', auth='public', type='http', cors='*', methods=['POST', 'GET'], csrf=False)
    def demo(self):
        return json.dumps({
            'bar1': json.loads(line_base()),
            'bar2': json.loads(gauge_base()),
        })


class PyEcharts(http.Controller):
    @http.route('/pyecharts', auth='public', type='http', cors='*', methods=['POST', 'GET'], csrf=False)
    def pyecharts(self):
        """
        {
            'column': 2 / 1,
            'detail': {
                sequence: {
                    'etype': etype,
                    'edata': edata,
                }
            }
        }
        :return:
        """
        # 1、get default dashboard
        dashboard_obj = request.env['echarts.dashboard'].p_get_default_dashboard()
        dashboard_dict = {
            'column': dashboard_obj.column,
            'count': len(dashboard_obj.line_ids),
            'theme': dashboard_obj.theme,
            'height': dashboard_obj.height,
            'details': [],
        }
        for line in dashboard_obj.line_ids:
            dashboard_dict['details'].append({
                'sequence': str(line.sequence),
                'etype': line.echart.etype,
                'edata': _get_chart(label=line.echart.etype),
            })
        return json.dumps(dashboard_dict)
        # return json.dumps({
        #     'bar1': json.loads(bar1_base()),
        #     'bar2': json.loads(bar2_base()),
        #     'bar3': json.loads(bar3_base()),
        #     'bar4': json.loads(bar4_base()),
        # })


def _get_chart(label=None):
    if label == 'Bar':
        return json.loads(bar_base())
    elif label == 'Pie':
        return json.loads(pie_base())
    elif label == 'Line':
        return json.loads(line_base())
    elif label == 'Gauge':
        return json.loads(gauge_base())
    elif label == 'Heatmap':
        return json.loads(heatmap_base())
    else:
        return {}


def bar_base():
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [random.randint(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [random.randint(0, 100) for _ in range(6)])
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Title", subtitle="Subtitle"),
                toolbox_opts=opts.ToolboxOpts(is_show=True, pos_left='90%', pos_top='top', feature={'saveAsImage': {}, 'dataView': {}}),
            )
            .dump_options_with_quotes()
    )
    return c


def pie_base():
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                legend_opts=opts.LegendOpts(is_show=True),
            )
            .dump_options_with_quotes()
    )
    return c


def line_base():
    x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]

    c = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True),
            toolbox_opts=opts.ToolboxOpts(is_show=True, pos_left='90%', pos_top='top'),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="",
                y_axis=y_data,
                symbol="emptyCircle",
                is_symbol_show=True,
                label_opts=opts.LabelOpts(is_show=True),
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
            .dump_options_with_quotes()
    )
    return c


def gauge_base():
    c = (
        Gauge()
            .add(
            "业务指标",
            [("完成率", 55.5)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
        )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Gauge-不同颜色"),
            legend_opts=opts.LegendOpts(is_show=False),
        ).dump_options_with_quotes()
    )
    return c


def heatmap_base():
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
            .add_xaxis(Faker.clock)
            .add_yaxis("series0", Faker.week, value)
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(),
        ).dump_options_with_quotes()
    )
    return c
