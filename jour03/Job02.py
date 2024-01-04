

class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        
    def afficher(self):
        print(f"Compte N°{self.__numero_compte}, Nom: {self.__nom}, Prénom: {self.__prenom}, Solde: {self.__solde}€")
    
    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde}€")
    
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant et aucun découvert autorisé.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def agios(self):
        if self.__solde < 0:
            print("Des agios seront appliqués en raison d'un solde négatif.")
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant pour effectuer le virement.")
        else:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            print(f"Virement de {montant}€ vers le compte N°{compte_destinataire.__numero_compte} effectué.")

# Création d'un compte bancaire et tests des méthodes
compte1 = CompteBancaire("123456", "Doe", "John", 1000)
compte1.afficher()
compte1.versement(500)
compte1.retrait(200)
compte1.afficherSolde()

# Ajout du découvert et tests supplémentaires
compte1.__decouvert = True  # normalement on ne devrait pas accéder directement à un attribut privé comme ça
compte1.retrait(1500)  # Retrait qui met le compte en découvert
compte1.agios()

# Création d'un second compte avec solde négatif et virement vers le premier compte pour remettre à zéro
compte2 = CompteBancaire("654321", "Doe", "Jane", -500, decouvert=True)
compte2.afficher()
compte2.virement(compte1, 500)
compte2.afficherSolde()
compte1.afficherSolde()
