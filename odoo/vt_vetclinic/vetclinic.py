from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
    _name = "vetclinic.animal"
    _columns = {
        'name': fields.char('Name', size=64),
        'birthday': fields.date('Birth Date'),
        'classication_id': fields.many2one('vetclinic.classification','Classification')
}

class vetclinic_classification(osv.Model):
    _name = "vetclinic.classification"
    _columns = {
        'name': fields.char('Name', size=32),  
        }

class vetclinic_breed(osv.Model):
    _name = "vetclinic.breed"
    _columns = {
        'name': fields.char('Name', size=32),  
        }    