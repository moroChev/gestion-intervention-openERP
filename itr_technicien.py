from openerp.osv import osv, fields
import openerp


class itr_technicien(osv.osv):
    _name = 'itr.technicien'
    _columns = {
        'nom': fields.char('Nom'),
        'taux_horaire': fields.integer('Taux Horaire'),
        'vol_horaire': fields.integer('Vol Horaire'),
        'cout': fields.float('Cout'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_technicien', string='Intervention')
    }

itr_technicien()
