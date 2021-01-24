from openerp.osv import osv, fields
import openerp

class itr_fournisseur(osv.osv):
    _name = 'itr.fournisseur'
    _columns = {
        'code': fields.char('Code'),
        'denomination': fields.char('Denomination'),
        'adresse': fields.char('Adresse'),
        'bon_commande_ids': fields.one2many('itr.bon_commande', 'id_fournisseur', string='Bon Commande'),
    }

itr_fournisseur()