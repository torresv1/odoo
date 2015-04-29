from openerp.osv import osv, fields
from openerp import api, models, _

import logging
_logger = logging.getLogger(__name__) # Need for message in console.

class product_template(osv.osv):
    _name = "product.template"
    _inherit = "product.template"
    _columns = {
        'boatlength':fields.char("Boat Length", size = 10),
        'fuelcapacity': fields.char("Fuel Capacity",size=10),
        'modeloptions_id': fields.many2one("product.category","Model Options"),
        'variantgroup_id': fields.many2one("product.variant_group","Variant Groups"),
    }

class product_product(osv.osv):
    _name = "product.product"
    _inherit = "product.product"


    def search(self,cr,uid,args,offset=0,limit=None, order=None, context=None,count=False):
        if context is None:
            context ={}

        if context.get('boatmodel_id'):
            #Code to limit by category assigned to the boat model.
            productobj =self.pool.get('product.product').read(cr,uid,context['boatmodel_id'],['modeloptions_id'])
            args = [('categ_id','=',productobj['modeloptions_id'][0])] + args


        return super(product_product, self).search(cr,uid,args,offset,limit,order,context=context,count=count)

class sale_order(osv.osv):
    _inherit = "sale.order"
    _columns = {
        'boatmodel_id':fields.many2one("product.product","Boat Model",domain=[('categ_id.name','=','Boat Models')]),
    }
    

class product_variant_group(osv.osv):
    _name = "product.variant_group"
    _columns = {
        'name':fields.char("Variant Group", size = 64),
        'description': fields.char("Description",size=10),
        'variants': fields.one2many('product.variant','variant_group_id', string = "Variants" ),
    }

class product_variant(osv.osv):
    _name = "product.variant"
    _columns = {
        'name':fields.char("Variant", size = 64),
        'description': fields.text("Description"),
        'variant_group_id':fields.many2one('product.variant_group','Variant Group'),
        
        }
    def name_search (self, cr, uid, name='',args=None, operator='ilike', context=None, limit=100 ):
        return super(product_variant, self).name_search(cr,uid,name,args,operator, context, limit)
        
             
class sale_order_line(osv.osv):
    _inherit = "sale.order.line"
    _columns = {
        'variant_id':fields.many2one("product.variant","Variant"),

    }
    

