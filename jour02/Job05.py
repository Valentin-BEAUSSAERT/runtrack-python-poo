class Voiture:
    def __init__(self, marque, modele, annee, kilometrage=0):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50 

    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque 
    
    def get_modele(self):
        return self.__modele
    
    def set_modele(self, modele):
        self.__modele = modele 
    
    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee 

    def get_kilometrage(self):
        return self.__kilometrage 
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage 

    def get_en_marche(self):
        return self.__en_marche 
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche 
    
    def get_reservoir(self):
        return self.__reservoir 
    
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir 
    
    def __verifier_plein(self):
        return self.__reservoir > 5
    
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est insuffisant.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")

voiture = Voiture("Peugeot", "208", 2015)

# Utilisation des méthodes 
voiture.demarrer()  # Démarre si le réservoir à minimum 5L
print("État de la voiture en marche:", voiture.get_en_marche())

voiture.arreter()   # Stop la voiture 
print("État de la voiture en marche:", voiture.get_en_marche())