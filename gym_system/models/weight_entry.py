# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WeightEntry(models.Model):
    _name = 'weight.entry'
    _rec_name = 'customer_id'
    _description = "Gym Exercise"

    customer_id = fields.Many2one('res.partner', string='Customer', )
    date = fields.Date(string='Date', )
    weight = fields.Float(string='Weight', )
