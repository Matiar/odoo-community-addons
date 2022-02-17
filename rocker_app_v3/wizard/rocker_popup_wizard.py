# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class rocker_popup_wizard(models.TransientModel):
    _name="rocker.popup.wizard"
    _description = "Popup wizard to display messages"
    
    def get_default(self):
        if self.env.context.get("message",False):
            return self.env.context.get("message")
        return False 

    name=fields.Text(string="Message",readonly=True,default=get_default)