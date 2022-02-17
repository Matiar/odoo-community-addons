from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

THEME_SELECTION = [
    ('shine', 'Shine'),
    ('dark', 'Dark'),
    ('roma', 'Roma'),
    ('vintage', 'Vintage'),
    ('macarons', 'Macarons'),
    ('infographic', 'Infographic'),
]


class Dashboard(models.Model):
    _name = 'echarts.dashboard'
    _description = 'Echarts Dashboard'

    name = fields.Char(string='Name')
    is_active = fields.Boolean(string='Active')
    column = fields.Integer(string='Column')
    theme = fields.Selection(THEME_SELECTION, default='shine', string='Theme')
    height = fields.Integer(default=400, string='Element Height（px）')

    line_ids = fields.One2many('echarts.dashboard.line', 'parent_id', string='Dashboard Detail')

    def p_get_default_dashboard(self):
        """

        :return:
        """
        dashboard = self.search([('is_active', '=', True)], limit=1)
        if dashboard:
            return dashboard


class DashboardLine(models.Model):
    _name = 'echarts.dashboard.line'
    _description = 'Echarts Dashboard Detail'

    parent_id = fields.Many2one('echarts.dashboard', string='Dashboard')
    sequence = fields.Integer(string='Sequence')
    echart = fields.Many2one('echarts.type', string='Echarts Type')
