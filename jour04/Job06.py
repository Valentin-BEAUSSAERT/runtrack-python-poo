# Création de la classe Vehicule avec la méthode démarrer
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

# Création de la classe Voiture héritant de Vehicule avec la méthode démarrer surchargée
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Attention, la voiture démarre avec classe")

# Création de la classe Moto héritant de Vehicule avec l'attribut roue et la méthode démarrer surchargée
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Attention, la moto vroom vroom sur la route")

# Instanciation et utilisation des objets Voiture et Moto
voiture = Voiture(marque="Peugeot", modele="208", annee=2018, prix=15000)
moto = Moto(marque="Yamaha", modele="MT-07", annee=2020, prix=7500)

# Affichage des informations et démarrage des véhicules
voiture.informationsVehicule()
voiture.demarrer()

moto.informationsVehicule()
moto.demarrer()
