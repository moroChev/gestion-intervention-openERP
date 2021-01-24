from openerp.osv import osv, fields
import openerp

class itr_intervention(osv.osv):
    _name = 'itr.intervention'
    _columns = {
        'code_intervention': fields.char('Code Intervention'),
        'date_demande': fields.date('Date Intervention'),
        'libelle_intervention': fields.char('Libelle Intervention'),
        'probleme': fields.char('Probleme'),
        'diagnostic': fields.char('Diagnostic'),
        'solution': fields.char('Solution'),
        'observation': fields.char('Observation'),
        'date_acceptee': fields.date('Date Acceptee'),
        'date_annulee': fields.date('Date Annulee'),
        'date_diagnostic': fields.date('Date Diagnostic'),
        'date_prepration': fields.date('Date Preparation'),
        'date_encours': fields.date('Date Encours'),
        'date_execute': fields.date('Date Execute'),
        'volume_horaire': fields.integer('Volume Horaire'),
        'cout_pdt': fields.float('Cout PDT'),
        'cout_interne': fields.float('Cout Interne'),
        'cout_prestation': fields.float('Cout Prestation'),
        'cout_global': fields.float('Cout Global'),
        'n_ordre_priorite': fields.integer('Nbr Ordre Priorite'),
        'id_personnel': fields.many2one('itr.personnel', 'Personnel', ondelete='cascade'),
        'id_patrimoine_geographique': fields.many2one('itr.patrimoine_geographique','Patrimoine Geographique', ondelete='cascade'),
        'id_patrimoine_actif': fields.many2one('itr.patrimoine_actif', 'Patrimoine Actif', ondelete='cascade'),
        'id_priorite': fields.many2one('itr.priorite', 'Priorite', ondelete='cascade'),
        'id_statut': fields.many2one('itr.statut', 'Statut', ondelete='cascade'),
        'id_unite': fields.many2one('itr.unite','Unite', ondelete='cascade'),
        'bon_commande_ids': fields.one2many('itr.bon_commande', 'id_intervention', string='Bon Commande'),
        'technicien_ids': fields.one2many('itr.technicien', 'id_intervention', string='Technicien'),
        'prestation_ids': fields.one2many('itr.prestation', 'id_intervention', string='Prestation'),
    }

itr_intervention()