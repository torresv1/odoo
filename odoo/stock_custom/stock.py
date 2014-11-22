from osv import osv,fields

class stock_picking(osv.osv):
    _inherit        = 'stock.picking'
    _columns        = {
                       'gross_weight'       : fields.float('Gross Weight'),
                       'tare'               : fields.float('Tare'),
                       'net_weight'         : fields.float('Net Weight'),
                       'user_note'          : fields.text('Notes'),
                       'create_uid'         : fields.many2one('res.users','Responsible',readonly=True),
                       }
    
    def onchange_weight(self,cr,uid,ids,gross,tare,contect=None):
        val = {}
        res = {'value':val}
        val['net_weight']       = gross - tare
        val['gross_weight']     = float(gross)
        val['tare']             = float(tare)
        return res
stock_picking()