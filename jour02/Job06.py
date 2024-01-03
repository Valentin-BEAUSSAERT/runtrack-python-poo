
class Commande:
    TAX_RATE = 0.20  

    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {} 
        self.__statut = "en cours" 
        self.__total = 0  

    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {'prix': prix, 'quantite': 1}
        else:
            self.__plats_commandes[nom_plat]['quantite'] += 1
        self.__total += prix
        print(f"Plat {nom_plat} ajouté avec succès.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__total = 0
        self.__statut = "annulée"
        print("La commande a été annulée.")

    def afficher_commande(self):
        for plat, details in self.__plats_commandes.items():
            print(f"{plat} - {details['quantite']}x - {details['prix']}€/unité")
        print(f"Total actuel de la commande: {self.__total}€")

    def calculer_TVA(self):
        return self.__total * Commande.TAX_RATE

    def afficher_total_avec_TVA(self):
        total_avec_TVA = self.__total + self.calculer_TVA()
        print(f"Total avec TVA: {total_avec_TVA}€")

ma_commande = Commande(1234)

ma_commande.ajouter_plat("Pizza", 12)
ma_commande.ajouter_plat("Salade", 8)
ma_commande.afficher_commande()
ma_commande.afficher_total_avec_TVA()

ma_commande.annuler_commande()
ma_commande.afficher_commande() 

