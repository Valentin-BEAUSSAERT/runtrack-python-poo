import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 10)  # Damage is random for simplicity
        adversaire.vie -= degats
        print(f"{self.nom} attaque et inflige {degats} points de dégâts à {adversaire.nom}!")

    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisir_niveau(self):
        self.niveau = input("Choisissez le niveau de difficulté (Facile, Moyen, Difficile): ").lower()

    def lancer_jeu(self):
        vies = {'facile': (100, 50), 'moyen': (100, 100), 'difficile': (50, 100)}
        vie_joueur, vie_ennemi = vies.get(self.niveau, (100, 100))

        self.joueur = Personnage("Joueur", vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        while self.joueur.est_vivant() and self.ennemi.est_vivant():
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.est_vivant():
                self.ennemi.attaquer(self.joueur)
        
        self.verifier_gagnant()

    def verifier_gagnant(self):
        if not self.joueur.est_vivant():
            print(f"{self.ennemi.nom} a gagné le combat!")
        else:
            print(f"{self.joueur.nom} a gagné le combat!")

jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
