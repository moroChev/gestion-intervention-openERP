from openerp.osv import osv, fields
import openerp


class itr_personnel(osv.osv):
    _name = 'itr.personnel'
    _columns = {
        'matricule': fields.char('Matricule'),
        'nom': fields.char('Nom'),
        'prenom': fields.char('Prenom'),
        'fonction': fields.char('Fonction'),
        'tel': fields.char('Telephone'),
        'fax': fields.char('Fax'),
        'email': fields.char('Email'),
        'intervention_ids': fields.one2many('itr.intervention', 'id_personnel', string='Intervention')
    }

itr_personnel()