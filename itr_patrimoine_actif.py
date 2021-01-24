from openerp.osv import osv, fields
import openerp


class itr_patrimoine_actif(osv.osv):
    _name = 'itr.patrimoine_actif'
    _columns = {
        'code': fields.char('Code'),
        'designation': fields.char('Designation'),
        'valeur_acquisition': fields.char('Valeur Acquisition'),
        'date_acquisition': fields.date('Date Acquisition'),
        'date_mise_service': fields.date('Date Mise En Service'),
        'etat_actuelle': fields.char('Etat Actuelle'),
        'n_bc': fields.char('N BC'),
        'n_bl': fields.char('N BL'),
        'n_facture': fields.char('N Facture'),
        'image_actif': fields.char('Image Actif'),
        'consigne_securite': fields.char('Consigne Securite'),
        'degre_importance': fields.char('Degre Importance'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_patrimoine_actif', string='Intervention')
    }


itr_patrimoine_actif()
