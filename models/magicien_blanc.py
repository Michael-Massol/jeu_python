import random
from models.personnage import Personnage

class MagicienBlanc(Personnage):
    """Le Magicien Blanc - Maître de la lumière et de la sagesse"""
    
    def __init__(self):
        super().__init__("✨ Gandalf le Blanc")
        self.frappes = [
            {"nom": "Éclair de Lumière", "force": 18, "xp": 5, "icone": "⚡"},
            {"nom": "Bâton de Pouvoir", "force": 22, "xp": 8, "icone": "🔆"},
            {"nom": "Flamme d'Anor", "force": 28, "xp": 12, "icone": "🔥"}
        ]
    
    def attaquer(self, cible):
        """Effectue une attaque avec une frappe aléatoire"""
        frappe_choisie = random.choice(self.frappes)
        print(f"{frappe_choisie['icone']} {self.nom} utilise: {frappe_choisie['nom']}")
        
        if self.frappe(cible, frappe_choisie["force"]):
            # Augmente l'expérience si la frappe a touché
            self.experience += frappe_choisie["xp"]
            print(f"✨ Expérience de {self.nom}: {self.experience}")