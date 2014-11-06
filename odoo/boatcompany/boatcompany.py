from openerp.osv import osv, fields

class product_product(osv.osv):
    _inherit = "product.product"
    _columns ={
        'boatlength': fields.char("Boat Length", size=10),
        'fuelcapacity':fields.char("Fuel Capacity", size=10),                 
               }