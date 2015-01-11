from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
    _name = "vetclinic.animal"
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'birthdate': fields.date('Birth Date'),
        'breed_id':fields.many2one('vetclinic.breed','Breed'),
        'classification_id': fields.many2one('vetclinic.classification','Classification', required=True),
        'labels_ids':fields.many2many('vetclinic.labels','rel_animal_labels','animal_id','labels_id',string='Label'),      
        'history':fields.text("History"),
        'res_partner_id': fields.many2one('res.partner','Owner'),
        'image':fields.binary("image"),
        'animal_vaccinations_ids':fields.one2many('vetclinic.animal_vaccinations','animal_id',string='Vaccinations'),
    }

class vetclinic_animal_vaccinations(osv.Model):
    _name = "vetclinic.animal_vaccinations"
    _columns = {
        'animal_id':fields.many2one('vetclinic.animal','Animal'),
        'product_id':fields.many2one('product.product','Vaccination'),
        'due_date':fields.date("Due Date"),
        'date_performed':fields.date("Date Performed"),        
        }

class vetclinic_res_partner(osv.Model):
    _inherit ="res.partner"
    _columns = {
        'animal_ids':fields.one2many('vetclinic.animal','res_partner_id',string='Pets'),
    }

class vetclinic_classification(osv.Model):
    _name = "vetclinic.classification"
    _columns = {
        'name': fields.char('Name', size=32), 
        'breed_ids':fields.one2many('vetclinic.breed','classification_id',string='Breeds'),
        }

class vetclinic_breed(osv.Model):
    _name = "vetclinic.breed"
    _columns = {
        'name': fields.char('Name', size=32),  
        'classification_id':fields.many2one('vetclinic.classification','Classification'),
        }
    
class vetclinic_labels(osv.Model):
    _name = "vetclinic.labels"
    _columns = {
        'name': fields.char('Name', size=32),  
        }            