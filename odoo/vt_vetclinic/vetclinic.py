from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
    _name = "vetclinic.animal"
    _columns = {
        'name': fields.char('Name', size=64),
        'birthdate': fields.date('Birth Date'),
        'breed_id':fields.many2one('vetclinic.breed','Breed'),
        'classification_id': fields.many2one('vetclinic.classification','Classification'),
        'labels_ids':fields.many2many('vetclinic.labels','rel_animal_labels','animal_id','labels_id',string='Label')      
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
    
class vetclinic_labels(osv.Model):
    _name = "vetclinic.labels"
    _columns = {
        'name': fields.char('Name', size=32),  
        }            