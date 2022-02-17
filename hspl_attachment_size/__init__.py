# Copyright 2018, 2021 Heliconia Solutions Pvt Ltd (https://heliconia.io)
from . import models

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["ir.model.data"].search([("model", "=", "ir.attachment")])
