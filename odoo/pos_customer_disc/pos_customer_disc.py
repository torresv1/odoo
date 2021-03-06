# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

import openerp
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class pos_customer_disc_c(osv.osv):
    _name = 'pos.customer.dsc.c'
    _description = "POS customer discount info"
    _columns = {
        'name': fields.char('Name', size=20),
        'value': fields.float('Discount Value', digits=(15,2)),

        }
pos_customer_disc_c()

    
class res_users(osv.osv):
    _inherit = 'res.partner'
    _columns = {

        'POS_discount_id': fields.many2one('pos.customer.dsc.c', 'POS discount', change_default=True, select=True, help="POS discount"),

    }

res_users()



