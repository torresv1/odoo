from osv import osv,fields
import base64
try:
    from reportlab.graphics.barcode import createBarcodeDrawing, \
            getCodes
except :
    print "ERROR IMPORTING REPORT LAB"

def _get_code(self, cr, uid, context=None):
    """get availble code """
    return [(r, r) for r in getCodes()]

class product_product(osv.osv):
    _inherit        = "product.product"
    #===========================================================================
    # FIRST ALTERLATIVE, CREATE BARCODE USING SAVE BUTTON
    #===========================================================================
    def get_barcode(self, value, width, hight, hr, code='UCPA'):
        options = {}
        if width:options['width'] = width
        if hight:options['hight'] = hight
        if hr:options['humanReadable'] = hr
        try:
            ret_val = createBarcodeDrawing(code, value=str(value), **options)
        except Exception, e:
            raise osv.except_osv('Error', e)
        return base64.encodestring(ret_val.asString('jpg'))

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            if obj.barcode_code:
                result[obj.id] = self.get_barcode(obj.barcode_code, width=0, hight=0, hr=obj.barcode_hr, code=obj.barcode_type)
            else:
                result[obj.id] = False
        return result
    
    #===========================================================================
    # SECOND ALTERNATIVE, CREATE BARCODE USING BUTTON
    #===========================================================================
    def get_image(self, value, width, hight, hr, code='QR'):
        options = {}
        if width:options['width'] = width
        if hight:options['hight'] = hight
        if hr:options['humanReadable'] = hr
        try:
            ret_val = createBarcodeDrawing(code, value=str(value), **options)
        except Exception, e:
            raise osv.except_osv('Error', e)
        return base64.encodestring(ret_val.asString('jpg'))
    
    def generate_image(self, cr, uid, ids, context=None):
        if not context:
            context = {}
        for self_obj in self.browse(cr, uid, ids, context=context):
            image = self.get_image(self_obj.code,
                        code=self_obj.barcode_type or 'qrcode',
                        width=self_obj.width, hight=self_obj.hight,
                        hr=self_obj.hr_form)
            self.write(cr, uid, self_obj.id,
                {'image':image},context=context)
        return True

    _columns        = {
                       'barcode_code'           : fields.char('Other Barcode',size=20),
                       'barcode_type'           : fields.selection(_get_code, 'Barcode Type'),
                       'barcode_hr'             : fields.boolean('Human Readable'),
                       'barcode_image'          : fields.function(_get_image, string="Image", type="binary"),
                       }
product_product()