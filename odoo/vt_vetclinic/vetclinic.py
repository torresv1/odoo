from openerp.osv import osv, fields

class vetclinic_animal(osv.Model):
    _name = "vetclinic.animal"
    _columns = {
        'name': field.char('Name', size=64),
        'birthday': field.date('Birth Date'),
}
    