# -*- coding: utf-8 -*-
################################################################################
#
# Computerized maintenance management system (CMMS) module,
# Copyright (C) 
#    2013 - Ait Mlouk Addi , (http://www.saghrosoft.com), All Right Reserved
#    2005 - 2011 Héonium (http://heonium.com). All Right Reserved
#
# CMMS module is free software: you can redistribute
# it and/or modify it under the terms of the Affero GNU General Public License
# as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# CMMS module is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Affero GNU
# General Public License for more details.
#
# You should have received a copy of the Affero GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from openerp.osv import osv, fields
import time
import pooler
import math
from tools import config
from openerp.tools.translate import _
import netsvc
import mx.DateTime
from mx.DateTime import RelativeDateTime, today, DateTime, localtime

class cmms_line(osv.osv):
    _name = 'cmms.line'
    _description = 'Production line'
    _columns = {
        'name': fields.char('Production line', size=64, required=True),
        'code': fields.char('Line reference', size=64),
        'location': fields.char('Location', size=64),
        'sequence': fields.integer('Sequence'),
    }

cmms_line()

class cmms_equipment(osv.osv):
    _name = "cmms.equipment"
    _description = "equipment"
    
    def create(self, cr, user, vals, context=None):
        if ('type' not in vals) or (vals.get('type')=='/'):
            vals['type'] = self.pool.get('ir.sequence').get(cr, user, 'cmms.equipment')
        return super(cmms_equipment, self).create(cr, user, vals, context)

    _columns = {
        'type': fields.char('Unit of work reference', size=64),
        'name': fields.char('Name', size=64 , required=True),
        'trademark': fields.char('Trademark', size=64),
        'active' : fields.boolean('Active'),
        'local_id': fields.many2one('stock.location', 'Location'),
        'line_id': fields.many2one('cmms.line','Production line', required=True, change_default=True),
        'invoice_id': fields.many2one('account.invoice', 'Purchase invoice'),
        'startingdate': fields.datetime("Starting date"),
        'product_ids': fields.many2many('product.product','product_equipment_rel','product_id','equipment_id','Piece of change'),
        'deadlinegar': fields.datetime("Deadline of guarantee"),
        'description': fields.text('Unit of work reference'),
        'safety': fields.text('Safety instruction'),
        'user_id': fields.many2one('res.users', 'Manager'),
    }
    _defaults = {
        'active' : lambda *a: True,
        'user_id': lambda object,cr,uid,context: uid,
        'type': lambda self, cr, uid, context: '/',
    }

    def copy(self, cr, uid, id, default=None, context=None):
        if context is None:
            context = {}
        if default is None:
            default = {}
        default = default.copy()
        default['type'] = self.pool.get('ir.sequence').get(cr, uid, 'cmms.equipment')
        return super(cmms_equipment, self).copy(cr, uid, id, default=default, context=context)
    
cmms_equipment()

