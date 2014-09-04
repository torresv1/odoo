from openerp.osv import osv,fields

class silkworm_sale_order_workflow(osv.Model):
    _inherit = 'sale.order'
    
    _columns = {
        'x_daterequired': fields.date('Date Required'),
        'x_rush': fields.boolean('Rush Order' ),
         
         'state':fields.selection([('cancel','Cancelled'),
                                   ('draft','Draft'),
                                   ('art_approved','Art Approved')
                                   ('confirmed','Confirmed'),
                                   ('exception','Exception'),
                                   ('done','Done')],
                                  'Status',required =True,
                                  readonly=True,help='n* The \'Draft\' status is set when the related sales order is in draft status.\ \n* The \'Confirmed\' status is set when the related sales order is confirmed.\ \n* The \'Exception\' status is set when the related sales order is set as exception.\ \n* The \'Done\' status is set when the related sales order is set as done.\\n* The \'Cancelled\' status is set when the related sales order is set at exception.\ '),
                }