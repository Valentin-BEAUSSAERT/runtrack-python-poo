# Définition de la classe Rectangle
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    # Assesseurs (Getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (Setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Définition de la classe Parallelepipede qui hérite de Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(longueur=5, largeur=3)

# Vérification des méthodes du rectangle
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

# Test des assesseurs et mutateurs
print("Longueur initiale:", rectangle.get_longueur())
print("Largeur initiale:", rectangle.get_largeur())

# Modification des attributs via mutateurs
rectangle.set_longueur(10)
rectangle.set_largeur(5)

# Vérification après modification
print("Nouvelle longueur:", rectangle.get_longueur())
print("Nouvelle largeur:", rectangle.get_largeur())
print("Nouveau périmètre après modification:", rectangle.perimetre())
print("Nouvelle surface après modification:", rectangle.surface())

# Instanciation et vérification de la classe Parallelepipede
parallelepipede = Parallelepipede(longueur=5, largeur=3, hauteur=4)
print("Volume du parallélépipède:", parallelepipede.volume())
