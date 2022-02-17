# Copyright 2018, 2021 Heliconia Solutions Pvt Ltd (https://heliconia.io)

import math

from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    size = fields.Char("File Size", compute="_compute_convert_size", store=True)

    @api.depends("file_size")
    def _compute_convert_size(self):
        """Compute for convert file size"""
        for rec in self:
            if rec.file_size == 0:
                return "0B"
            size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
            i = int(math.floor(math.log(rec.file_size, 1024)))
            p = math.pow(1024, i)
            s = round(rec.file_size / p, 2)
            rec.size = "%s %s" % (s, size_name[i])
