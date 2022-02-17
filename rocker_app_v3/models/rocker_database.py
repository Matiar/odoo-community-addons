# -*- coding: utf-8 -*-
#############################################################################
#
#    Copyright (C) 2019-Antti Kärki.
#    Author: Antti Kärki.
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import api, fields, models
from odoo import exceptions
import logging

from . import rocker_connection

_logger = logging.getLogger(__name__)


class rocker_database(models.Model):
    _name = 'rocker.database'
    _description = 'Rocker Reporting Databases'
    name = fields.Char('Title', required=True, default='Odoo')
    _sql_constraints = [('unique_name', 'UNIQUE(name)', 'Datasource Name must be unique')]
    driver = fields.Selection(
        [('mysql', 'MySQL'), ('mariadb', 'MariaDB'), ('oracle', 'Oracle'), ('sqlserver', 'SQLServer'), ('odbc', 'ODBC'),
         ('postgresql', 'PostrgeSQL')], 'Driver', required=True, default='postgresql')
    odbcdriver = fields.Char('ODBC driver', required=False, default='SQL Server')
    # sid = fields.Char('Oracle SID', required=False)
    host = fields.Char('Host', required=True, default='127.0.0.1')
    port = fields.Char('Port', required=False, default='5432')
    database = fields.Char('Database or SID ', required=True, default='Rocker')
    user = fields.Char('User', required=True, default='openpg')
    password = fields.Char('Password', required=True, default='openpgpwd')

    # @api.multi
    def testconnection(self):
        _datasource = self.name
        _driver = self.driver
        _odbcdriver = self.odbcdriver
        _sid = self.database
        _database = self.database
        _host = self.host
        _port = self.port
        _user = self.user
        _password = self.password
        con = None
        _logger.info('Testing connection to ' + self.name)

        context = {}
        title = ''
        con = rocker_connection.rocker_connection.create_connection(self)
        if con:
            context['message'] = "Connection succesful"
            title = 'Success'
            con.close()
        else:
            context['message'] = "Connection failed"
            title = 'Error'
        view = self.env.ref('rocker_app_v3.rocker_popup_wizard')
        view_id = False
        return {
            'name': title,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'rocker.popup.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }
