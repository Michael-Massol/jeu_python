import time
from models.personnage import Personnage
from utils.utils import afficher_titre, afficher_introduction, afficher_vainqueur

class Combat:
    """Gère le déroulement d'un combat entre deux personnages"""
    
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tour_numero = 1
    
    def demarrer(self):
        """Démarre et gère le combat jusqu'à la victoire"""
        afficher_titre()
        afficher_introduction(self.joueur1, self.joueur2)
        
        time.sleep(1)
        
        # Boucle de combat
        while self.joueur1.est_vivant() and self.joueur2.est_vivant():
            self._executer_tour()
            time.sleep(1.5)
            self.tour_numero += 1
            
            # Limite de sécurité pour éviter un combat infini
            if self.tour_numero > 50:
                print("\\n⏱️  Le combat dure trop longtemps... Match nul !")
                return
        
        # Annonce du vainqueur
        self._annoncer_resultat()
    
    def _executer_tour(self):
        """Exécute un tour de combat"""
        print(f"\\n{'='*60}")
        print(f"🎯 TOUR {self.tour_numero}".center(60))
        print(f"{'='*60}")
        
        if Personnage.tour == 'joueur1':
            self.joueur1.attaquer(self.joueur2)
            Personnage.tour = 'joueur2'
        else:
            self.joueur2.attaquer(self.joueur1)
            Personnage.tour = 'joueur1'
    
    def _annoncer_resultat(self):
        """Annonce le résultat final du combat"""
        print("\\n" + "="*60)
        print("🏆 FIN DU COMBAT 🏆".center(60))
        print("="*60)
        
        if self.joueur1.est_vivant():
            afficher_vainqueur(self.joueur1, "💡 La lumière triomphe des ténèbres !")
        else:
            afficher_vainqueur(self.joueur2, "🌑 Les ténèbres enveloppent la Terre du Milieu !")
        
        print("\\n" + "="*60)