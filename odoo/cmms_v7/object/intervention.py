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

from mx import DateTime
import time
import netsvc
from osv import fields, osv
from tools import config
from openerp.tools.translate import _
import tools

class cmms_intervention(osv.osv):
    _name = "cmms.intervention"
    _description = "Intervention request"

    def create(self, cr, user, vals, context=None):
        if ('name' not in vals) or (vals.get('name')=='/'):
            vals['name'] = self.pool.get('ir.sequence').get(cr, user, 'cmms.intervention')
        return super(cmms_intervention, self).create(cr, user, vals, context)

    _columns = {
        'name': fields.char('Intervention reference', size=64),
        'equipment_id': fields.many2one('cmms.equipment', 'Unit of work', required=True),
        'date': fields.datetime('Date'),
        'user_id': fields.many2one('res.users', 'Sender', readonly=True),
        'user2_id': fields.many2one('res.users', 'Recipient'),
        'priority': fields.selection([('normal','Normal'),('low','Low'),('urgent','Urgent'),('other','Other')],'priority', size=32),
        'observation': fields.text('Observation'),
        'date_inter': fields.datetime('Intervention date'),
        'date_end': fields.datetime('Intervention end date'),
        'type': fields.selection([('check','Check'),('repair','Repair'),('revision','Revision'),('other','Other')],'Intervention type', size=32),
    }
    _defaults = {
        'type': lambda * a:'repair',
        'priority': lambda * a:'normal',
        'user_id': lambda object,cr,uid,context: uid,
        'date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'name': lambda self, cr, uid, context: '/',
    }

    def copy(self, cr, uid, id, default=None, context=None):
        if not context:
            context = {}
        if default is None:
            default = {}
            default = default.copy()
            default['name'] = self.pool.get('ir.sequence').get(cr, uid, 'cmms.intervention')
        return super(cmms_intervention, self).copy(cr, uid, id, default=default, context=context)

cmms_intervention()
