import math 

# Création de la classe Forme
class Forme:
    def aire(self):
        return 0

# Création de la classe Rectangle héritant de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=5, hauteur=10)
print("L'aire du rectangle est:", rectangle.aire())

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

# Création d'instances de Rectangle et Cercle
rectangle = Rectangle(largeur=5, hauteur=10)
cercle = Cercle(radius=7)

# Affichage des résultats des méthodes aire pour chaque instance
print("L'aire du rectangle est:", rectangle.aire())
print("L'aire du cercle est:", cercle.aire())