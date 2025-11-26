from models.magicien_blanc import MagicienBlanc
from models.roi_sorcier import RoiSorcier
from jeu.combat import Combat

def main():
    """Point d'entrée principal du programme"""
    
    # Création des combattants
    magicien = MagicienBlanc()
    roi_sorcier = RoiSorcier()
    
    # Création et démarrage du combat
    combat = Combat(magicien, roi_sorcier)
    combat.demarrer()

if __name__ == "__main__":
    main()