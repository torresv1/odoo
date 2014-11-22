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
{
    "name": "Computerized maintenance management system",
    "version": "1.1",
    "depends": ["base", "product", "stock"],
    "author": "Héonium /Ait Mlouk Addi ",
    'website': 'http://heonium.com - http://www.iminoika.com',
    "category": "Specific Modules/CMMS",
    "description": """
Computerized maintenance management system module allow you to manage 
preventives and corrective maintenance without limit.
All informations is linked to the equipment tree and let you follow 
maintenance operation :
 - Repair.
 - Check up List.
 - ...
With this module you can following all equipment type.
""",
    "init_xml": [],
    'update_xml': [
        'security/cmms_security.xml',
        'security/ir.model.access.csv',
        'view/equipment_view.xml',
        'view/checklist_view.xml',
        'view/cm_view.xml',
        'view/intervention_view.xml',
        'view/incident_view.xml',
        'view/pm_view.xml',
        'view/cmms_view.xml',
        'data/cmms_sequence.xml',
        'data/cmms_demo.xml',
        'gmao_menu.xml',
        
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
