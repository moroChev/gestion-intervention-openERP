from openerp.osv import osv, fields
import openerp

class itr_bon_commande(osv.osv):
    _name = 'itr.bon_commande'
    _columns = {
        'code_bc': fields.char('Code'),
        'date_bc': fields.date('Denomination'),
        'montant_bc_ht': fields.integer('Montant Bon Commande HT'),
        'montant_bc_ttc': fields.integer('Montant Bon Commande TTC'),
        'id_fournisseur': fields.many2one('itr.fournisseur', ondelete='cascade'),
        'id_intervention': fields.many2one('itr.itervention', ondelete='cascade'),
    }

itr_bon_commande()