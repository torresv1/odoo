from openerp.osv import osv, fields


class product_template(osv.osv):
    _name = "product.template"
    _inherit = "product.template"
    _columns = {
        'boatlength':fields.char("Boat Length", size = 10),
        'fuelcapacity': fields.char("Fuel Capacity",size=10),
    }


