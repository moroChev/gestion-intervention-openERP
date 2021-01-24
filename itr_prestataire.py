from openerp.osv import osv, fields
import openerp

class itr_prestataire(osv.osv):
    _name = 'itr.prestataire'
    _columns = {
        'prestataire': fields.char('Prestataire'),
        'prestation_ids': fields.one2many('itr.prestation', 'id_prestataire', string='Prestation'),
    }

itr_prestataire()