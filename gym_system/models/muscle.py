# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Muscle(models.Model):
    _name = 'gym.muscle'
    name = fields.Char(string='Name')
    description = fields.Text(string='Description', )
    image = fields.Binary(string='Image', store=True, )
    typeside = fields.Selection([('front_side', 'Front Side'), ('back_side', 'Back Side')], string='Type', )
    exercise_category_id = fields.Many2many('exercise.category.select', string='Exercise Category')

