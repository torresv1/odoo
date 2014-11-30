from openerp.osv import osv, fields


class product_template(osv.osv):
    _name = "product.template"
    _inherit = "product.template"
    _columns = {
        'boatlength':fields.char("Boat Length", size = 10),
        'fuelcapacity': fields.char("Fuel Capacity",size=10),
        'modeloptions_id': fields.many2one("product.category","Model Options"),
    }
    def search(self,cr,uid,args,offset=0,limit=None, order=None, context=None,count=False):
        if context is None:
            context ={}
            
            """ Check to see if we get have the ‘boatmodel_id’ passed in context.  
            This will keep the search from breaking when we are using it for searches outside
            of the sales order form."""  
                
        if context.get('boatmodel_id'):
            
            #Code to limit by category assigned to the boat model.
            
            productobj =self.pool.get('product.product').read(cr,uid,context['boatmodel_id'],['modeloptions_id']) 
          
        return super(product_template, self).search(cr,uid,args,offset,limit,order,context=context,count=count)

class sale_order(osv.osv):
    _inherit = "sale.order"
    _columns = {
        'boatmodel_id':fields.many2one("product.product","Boat Model",domain=[('categ_id.name','=','Boat Models')]),
    }
    
    
