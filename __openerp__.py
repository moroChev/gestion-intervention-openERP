
{
    'name' : "Gestion des interventions",
    'version' : '1.0',
    'author' : 'Mohcine Rouessi - Mohammed Hibat Allah',
    'category' : 'ENSAH ERP',
	'sequence' :1,
    'description' : """
	------------------------------------------
    ------------------------------------------
    
   """,
    'website': 'http://www.monsite.ma',
    'images' : [''],
    'depends' : ['base'],
    'data': [
            'itr_bon_commande_view.xml',
            'itr_fournisseur_view.xml',
            'itr_intervention_view.xml',
            'itr_patrimoine_actif_view.xml',
            'itr_patrimoine_geographique_view.xml',
            'itr_personnel_view.xml',
            'itr_prestataire_view.xml',
            'itr_prestation_view.xml',
            'itr_priorite_actif_view.xml',
            'itr_statut_view.xml',
            'itr_technicien_view.xml',
            'itr_unite_view.xml',
            'itr_patrimoine_geographique_view.xml'
            ],
    'update_xml': [ ],
    'js': [],
    'qweb' : [],
    'css':[''],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
