from openerp.osv import osv, fields
import openerp

class itr_statut(osv.osv):
    _name = 'itr.statut'
    _columns = {
        'statut': fields.char('Statut'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_statut', string='Intervention')
    }

itr_statut()