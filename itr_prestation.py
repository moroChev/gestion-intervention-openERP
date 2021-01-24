from openerp.osv import osv, fields
import openerp

class itr_prestation(osv.osv):
    _name = 'itr.prestation'
    _columns = {
        'vol_horaire': fields.integer('Horaire du Vol'),
        'cout': fields.float('Cout'),
        'id_intervention': fields.many2one('itr.itervention', ondelete='cascade'),
        'id_prestataire': fields.many2one('itr.prestataire', ondelete='cascade')
    }

itr_prestation()