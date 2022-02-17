# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExerciseCategory(models.Model):
    _name = 'exercise.category'
    _rec_name = 'exercise_category_id'

    category = fields.Selection([('acehold', 'Axe Hold'),
                                 ('barbell tricep extension', 'Barbell Tricep Extension')], string='Exercise',
                                )
    name = fields.Char(string='Select Your Exercise', )
    description = fields.Text(string='Description', )
    muscles_id = fields.Many2many('gym.muscle', string='Affected Muscles', )
    equipment_id = fields.Many2one('product.product', string='Equipment', )
    image = fields.Binary(string='Image', )
    exercise_id = fields.Many2one('exercise.select', string='Exercise On', )
    exercise_category_id = fields.Many2one('exercise.category.select', string='Exercise', )

