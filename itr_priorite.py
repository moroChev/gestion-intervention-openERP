from openerp.osv import osv, fields
import openerp

class itr_priorite(osv.osv):
    _name = 'itr.priorite'
    _columns = {
        'priorite': fields.char('Priorite'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_priorite', string='Intervention')
    }

itr_priorite()