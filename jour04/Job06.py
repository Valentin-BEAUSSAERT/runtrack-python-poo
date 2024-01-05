# Création de la classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}")

# Création de la classe Voiture héritant de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

# Instanciation d'un objet Voiture avec les informations nécessaires
voiture = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)

# Appel à la méthode informationsVehicule de l'objet voiture
voiture.informationsVehicule()
