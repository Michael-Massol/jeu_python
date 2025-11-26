import random
from models.personnage import Personnage

class RoiSorcier(Personnage):
    """Le Roi Sorcier d'Angmar - Seigneur des Nazgûl"""
    
    def __init__(self):
        super().__init__("👑 Roi Sorcier d'Angmar")
        self.frappes = [
            {"nom": "Lame Maudite", "force": 20, "xp": 6, "icone": "🗡️"},
            {"nom": "Cri Spectral", "force": 24, "xp": 9, "icone": "👻"},
            {"nom": "Ténèbres Dévorantes", "force": 26, "xp": 11, "icone": "🌑"}
        ]
    
    def attaquer(self, cible):
        """Effectue une attaque avec une frappe aléatoire"""
        frappe_choisie = random.choice(self.frappes)
        print(f"{frappe_choisie['icone']} {self.nom} utilise: {frappe_choisie['nom']}")
        
        if self.frappe(cible, frappe_choisie["force"]):
            # Augmente l'expérience si la frappe a touché
            self.experience += frappe_choisie["xp"]
            print(f"💀 Expérience de {self.nom}: {self.experience}")