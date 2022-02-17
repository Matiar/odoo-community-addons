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

_logger = logging.getLogger(__name__)


class rocker_connection():

    # @api.multi
    #
    def create_connection(self):

        _database_record = self
        _datasource = _database_record.name
        _driver = _database_record.driver
        _odbcdriver = _database_record.odbcdriver
        _sid = _database_record.database
        _database = _database_record.database
        _host = _database_record.host
        _port = _database_record.port
        _user = _database_record.user
        _password = _database_record.password

        con = None
        _logger.info('Connecting to database: ' + _database)

        try:
            if _driver == 'postgresql':
                try:
                    import psycopg2
                except:
                    raise exceptions.ValidationError('No Postgres drivers')
                con = psycopg2.connect(host=_host, port=_port, database=_database, user=_user, password=_password)
            elif _driver == "mysql":
                try:
                    import mysql.connector
                except:
                    raise exceptions.ValidationError('No MySQL drivers')
                con = mysql.connector.connect(host=_host, port=_port, database=_database, user=_user,
                                              password=_password)
            elif _driver == "mariadb":
                try:
                    import mysql.connector
                except:
                    raise exceptions.ValidationError('No MariaDB drivers')
                con = mysql.connector.connect(host=_host, port=_port, database=_database, user=_user,
                                              password=_password)
            elif _driver == "oracle":
                _logger.debug('Try Oracle')
                _logger.debug(_user + '/' + _password + '@' + _host + ':' + _port + '/' + _sid)
                try:
                    import cx_Oracle
                    # cx_Oracle.init_oracle_client()
                    con = cx_Oracle.connect(_user + '/' + _password + '@' + _host + ':' + _port + '/' + _sid)
                except Exception as err:
                    _logger.debug("Whoops in Oracle connect!")
                    _logger.debug(err)
                    raise exceptions.ValidationError('Oracle drivers\n'+err)

            # con = cx_Oracle.connect("user", "passwd", "192.168.1.88:1521/xe")
            elif _driver == "sqlserver":
                try:
                    import pyodbc
                except:
                    raise exceptions.ValidationError('No SQLServer (ODBC) drivers')
                _logger.debug(
                    'DRIVER={' + _odbcdriver + '};SERVER=' + _host + ';DATABASE=' + _database + ';UID=' + _user + ';PWD=' + _password)
                con = pyodbc.connect(
                    'DRIVER={' + _odbcdriver + '};SERVER=' + _host + ';DATABASE=' + _database + ';UID=' + _user + ';PWD=' + _password)
                self._sqldriver = 'sqlserver'
            elif _driver == "odbc":
                try:
                    import pyodbc
                except:
                    raise exceptions.ValidationError('No ODBC drivers')
                _logger.debug(
                    'DRIVER={' + _odbcdriver + '};SERVER=' + _host + ';DATABASE=' + _database + ';UID=' + _user + ';PWD=' + _password)
                con = pyodbc.connect(
                    'DRIVER={' + _odbcdriver + '};SERVER=' + _host + ';DATABASE=' + _database + ';UID=' + _user + ';PWD=' + _password)
                self._sqldriver = 'odbc'
            else:
                raise exceptions.ValidationError('Driver not supported')
        except:
            _logger.debug('Database connection failed')
            raise exceptions.ValidationError('Database connection failed')
        return con
