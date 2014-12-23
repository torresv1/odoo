from openerp.osv import osv, fields


class product_template(osv.osv):
    _name = "product.template"
    _inherit = "product.template"
    _columns = {
        'boatlength':fields.char("Boat Length", size = 10),
        'fuelcapacity': fields.char("Fuel Capacity",size=10),
        'modeloptions_id': fields.many2one("product.category","Model Options"),
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
    
    
