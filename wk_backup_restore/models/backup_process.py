# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#
#################################################################################

from odoo import fields, api, models
from odoo.exceptions import UserError
from odoo.tools.config import config

from odoo.addons.wk_backup_restore.models.lib import manage_backup_crons
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


LOCATION = [
    ('local', 'Local'),
]

CYCLE = [
    ('half_day', 'Twice a day'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
]

STATE = [
    ('draft', 'Draft'),
    ('confirm', 'Confirm'),
    ('running', 'Running'),
    ('cancel', 'Cancel')
]

class BackupProcess(models.Model):
    _name = "backup.process"


    def _default_db_name(self):
        return self._cr.dbname

    name = fields.Char(string="Process Name")
    frequency = fields.Integer(string="Frequency", default=1)
    frequency_cycle = fields.Selection(selection=CYCLE, string="Frequency Cycle")
    storage_path = fields.Char(string="Storage Path")
    backup_location = fields.Selection(selection=LOCATION, string="Backup Location", default="local")
    retention = fields.Integer(string="Backup Retention")
    start_time = fields.Datetime(string="Backup Starting Time")
    db_name = fields.Char(string="Database Name", default=_default_db_name)
    backup_starting_time = fields.Datetime(string="Backup Starting Time")
    state = fields.Selection(selection=STATE, default='draft')
    update_requested = fields.Boolean(string="Update Requested", default=False)
    master_pass = fields.Char(string="Master Password")
    backup_details_ids = fields.One2many(comodel_name="backup.process.detail", inverse_name="backup_process_id", string="Backup Details")


    @api.onchange('frequency_cycle')
    def change_frequency_value(self):
        if self.frequency_cycle == 'half_day':
            self.frequency = 2
        else:
            self.frequency = 1

    def call_backup_script(self, master_pass=None, port_number=None, url=None, db_user=None, db_password=None):
        _logger.info("++++++++   script finally called-- master_pass--------- %r "%master_pass)
        _logger.info("++++++++   script finally called--- url -------- %r "%url)
        db_user = config.get('db_user')
        db_password = config.get('db_password')
        res = manage_backup_crons.add_cron(master_pass=master_pass, main_db=self._cr.dbname, db_name=self.db_name, backup_location=self.backup_location, frequency=self.frequency, frequency_cycle=self.frequency_cycle, storage_path=self.storage_path, url=url, db_user=db_user, db_password=db_password, process_id=self.id)
        _logger.info("--------- Got the return   %r ------------"%res)
        if res.get('success'):
            self.state = 'running'
            return res

    def update_backup_request(self):
        _logger.info("------   Args to update script db_name -- %r "%self.db_name)
        _logger.info("------   Args to update script frequency -- %r "%self.frequency)
        _logger.info("------   Args to update script frequency_cycle -- %r "%self.frequency_cycle)
        res = manage_backup_crons.update_cron(db_name=self.db_name, frequency=self.frequency, frequency_cycle=self.frequency_cycle)
        _logger.info(" ++  ==Update method  == ==   %r ====== "%res)
        if res.get('success'):
            self.update_requested = False
    
    def create_backup_request(self):
        master_pass = self.master_pass
        url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return self.call_backup_script(master_pass=master_pass, url=url)

    def remove_attached_cron(self):
        if self.state == 'running':
            res = manage_backup_crons.remove_cron(db_name=self.db_name, frequency=self.frequency, frequency_cycle=self.frequency_cycle)
        else:
            res = dict(
                success = True
            )
        _logger.info(" ++  ==Remove method  == ==   %r ====== "%res)
        if res.get('success'):
            self.state = 'cancel'
            return res
    
    @api.model
    def ignite_backup_server_crone(self):
        current_time = datetime.now()
        processes = self.env['backup.process'].sudo().search([('backup_starting_time', '<=', current_time), ('state', '=', 'confirm')])
        for process in processes:
            process.create_backup_request()
        _logger.info("########333  %r ######## processes"%processes)
        upt_processes = self.env['backup.process'].sudo().search([('backup_starting_time', '<=', current_time), ('state', '=', 'running'), ('update_requested', '=', True)])        
        _logger.info("########333  %r ######## processes"%upt_processes)        
        for upt_process in upt_processes:
            if upt_process.update_requested:
                upt_process.update_backup_request()

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('backup.process')
        res = super(BackupProcess, self).create(vals)
        return res

    def unlink(self):
        raise UserError("Not allowed")

    def confirm_process(self):
        if self.state == 'draft':
            self.state ="confirm"
