from osv import osv, fields

class vetclinic_animal(osv.Model):
    _name = "vetclinic.animal"
    _columns = {
        'name': fields.char('Name', size=64),
        'birthday': fields.date('Birth Date'),
}
    