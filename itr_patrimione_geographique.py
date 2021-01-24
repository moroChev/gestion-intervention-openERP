from openerp.osv import osv, fields
import openerp

class itr_patrimoine_geographique(osv.osv):
    _name = 'itr.patrimoine_geographique'
    _columns = {
        'code': fields.char('Code'),
        'designation': fields.char('Designation'),
        'croquis': fields.char('Croquis'),
        'fiche_immeuble': fields.char('Fiche Immeuble'),
        'fiche_etage': fields.char('Fiche Etage'),
        'fiche_local': fields.char('Fiche Local'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_patrimoine_geographique', string='Intervention')
    }

itr_patrimoine_geographique()