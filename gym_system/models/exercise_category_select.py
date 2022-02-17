# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExerciseCategorySelect(models.Model):
    _name = 'exercise.category.select'
    _rec_name = 'name'

    name = fields.Char( string='Exercise',required=True,    )
    body_parts_id = fields.Many2one( 'exercise.select', string='Body Part',)
