class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur 
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur 

    def __str__(self):
        return f"Rectangle (longueur = {self.__longueur}, largeur = {self.__largeur})"

rectangle_instance = Rectangle(10, 5)

etat_initial = str(rectangle_instance)
print(etat_initial)

rectangle_instance.set_longueur(15)
rectangle_instance.set_largeur(10)

etat_modifie = str(rectangle_instance)
print(etat_modifie)

(etat_initial, etat_modifie)