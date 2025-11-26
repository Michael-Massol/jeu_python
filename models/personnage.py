from abc import ABC, abstractmethod

class Personnage(ABC):
    """Classe abstraite représentant un personnage de combat"""
    
    tour = 'joueur1'  # Variable de classe publique
    
    def __init__(self, nom):
        self._nom = nom
        self._vie = 100
        self._frappes = []
        self._experience = 0
        self._degats = 0
    
    # Getters et Setters avec validation
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str) or len(valeur) == 0:
            raise ValueError("Le nom doit être une chaîne non vide")
        self._nom = valeur
    
    @property
    def vie(self):
        return self._vie
    
    @vie.setter
    def vie(self, valeur):
        if not isinstance(valeur, (int, float)) or valeur < 0:
            raise ValueError("La vie doit être un nombre positif")
        self._vie = valeur
    
    @property
    def frappes(self):
        return self._frappes
    
    @frappes.setter
    def frappes(self, valeur):
        if not isinstance(valeur, list):
            raise ValueError("Les frappes doivent être une liste")
        self._frappes = valeur
    
    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, valeur):
        if not isinstance(valeur, (int, float)) or valeur < 0:
            raise ValueError("L'expérience doit être un nombre positif")
        self._experience = valeur
    
    @property
    def degats(self):
        return self._degats
    
    @degats.setter
    def degats(self, valeur):
        if not isinstance(valeur, (int, float)) or valeur < 0:
            raise ValueError("Les dégâts doivent être un nombre positif")
        self._degats = valeur
    
    def frappe(self, cible, force_frappe):
        """Effectue une frappe sur la cible"""
        print(f"\\n⚔️  {self.nom} attaque {cible.nom} !")
        
        # Tentative d'esquive
        if cible.esquive():
            print(f"💨 {cible.nom} esquive l'attaque !")
            return False
        else:
            cible.recoit_degat(self, force_frappe)
            return True
    
    def esquive(self):
        """Tente d'esquiver une attaque (25% de chance)"""
        import random
        return random.random() < 0.25
    
    def recoit_degat(self, adversaire, force_frappe):
        """Reçoit des dégâts d'un adversaire"""
        degats_totaux = force_frappe + adversaire.experience
        self.degats += degats_totaux
        vie_restante = max(0, self.vie - self.degats)
        
        print(f"💥 {self.nom} reçoit {degats_totaux:.1f} points de dégâts !")
        print(f"❤️  Vie restante de {self.nom}: {vie_restante:.1f}/{self.vie}")
    
    def est_vivant(self):
        """Vérifie si le personnage est encore en vie"""
        return self.degats < self.vie
    
    @abstractmethod
    def attaquer(self, cible):
        """Méthode abstraite pour attaquer (à implémenter par les sous-classes)"""
        pass