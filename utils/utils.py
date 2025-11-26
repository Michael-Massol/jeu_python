def afficher_titre():
    """Affiche le titre du jeu"""
    print("\\n" + "="*60)
    print("⚔️  BATAILLE ÉPIQUE EN TERRE DU MILIEU ⚔️".center(60))
    print("="*60)

def afficher_introduction(joueur1, joueur2):
    """Affiche l'introduction du combat"""
    print(f"\\n{joueur1.nom} VS {joueur2.nom}")
    print(f"❤️  Vie: {joueur1.vie} | ❤️  Vie: {joueur2.vie}")
    print("\\n" + "="*60)

def afficher_vainqueur(vainqueur, message):
    """Affiche les informations du vainqueur"""
    print(f"\\n🎉 {vainqueur.nom} remporte la victoire !")
    print(f"✨ Vie restante: {vainqueur.vie - vainqueur.degats:.1f}")
    print(f"⭐ Expérience finale: {vainqueur.experience}")
    print(f"\\n{message}")

def creer_separateur(caractere="=", longueur=60):
    """Crée une ligne de séparation"""
    return caractere * longueur

def afficher_statistiques(personnage):
    """Affiche les statistiques d'un personnage"""
    vie_restante = max(0, personnage.vie - personnage.degats)
    print(f"\\n📊 Statistiques de {personnage.nom}:")
    print(f"   ❤️  Vie: {vie_restante:.1f}/{personnage.vie}")
    print(f"   💥 Dégâts subis: {personnage.degats:.1f}")
    print(f"   ⭐ Expérience: {personnage.experience}")