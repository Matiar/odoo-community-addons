# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CalorieCal(models.Model):
    _name = 'gym.calorie'
    _rec_name = 'name_id'

    name_id = fields.Many2one('res.partner', string='Name',
                              )
    age = fields.Float(string='Age', )
    height = fields.Float(string='Height', )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender',
                              )
    weight = fields.Float(string='Weight', )
    bmr = fields.Float(string='BMR', compute='_compute_bmr', )


    @api.depends('height', 'weight', 'age')
    def _compute_bmr(self):
        for rec in self:
            rec.bmr = 66.47 + \
                      (13.75 * rec.weight) + (5.0 * rec.height) - (6.75 * rec.age)
