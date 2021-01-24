from openerp.osv import osv, fields
import openerp

class itr_unite(osv.osv):
    _name = 'itr.unite'
    _columns = {
        'code': fields.char('Code'),
        'designation': fields.char('Designation'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_unite', string='Intervention')
    }

itr_unite()
