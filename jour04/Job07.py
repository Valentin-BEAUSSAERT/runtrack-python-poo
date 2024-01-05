import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs]
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def valeur_carte(self, carte):
        if carte.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif carte.valeur == 'As':
            return 11
        else:
            return int(carte.valeur)

    def total_main(self, main):
        total = sum(self.valeur_carte(carte) for carte in main)
        for carte in main:
            if carte.valeur == 'As' and total > 21:
                total -= 10
        return total

    def jouer(self):
        main_joueur, main_croupier = [self.tirer_carte() for _ in range(2)], [self.tirer_carte() for _ in range(2)]
        print(f"Votre main: {main_joueur}, total: {self.total_main(main_joueur)}")
        print(f"Main du croupier: [{main_croupier[0]}, X]")

        # Tour du joueur
        choix = input("Voulez-vous tirer une carte ? (o/n) ")
        while choix.lower() == 'o':
            carte = self.tirer_carte()
            main_joueur.append(carte)
            total_joueur = self.total_main(main_joueur)
            print(f"Vous avez tiré: {carte}, total: {total_joueur}")
            if total_joueur > 21:
                print("Désolé, vous avez perdu !")
                return
            choix = input("Voulez-vous tirer une autre carte ? (o/n) ")

        # Tour du croupier
        while self.total_main(main_croupier) < 17:
            carte = self.tirer_carte()
            main_croupier.append(carte)

        total_croupier = self.total_main(main_croupier)
        print(f"Main du croupier: {main_croupier}, total: {total_croupier}")

        # Résultat
        if total_croupier > 21 or self.total_main(main_joueur) > total_croupier:
            print("Félicitations, vous avez gagné !")
        else:
            print("Désolé, le croupier gagne.")

# Jouer une partie
jeu = Jeu()
jeu.jouer()
