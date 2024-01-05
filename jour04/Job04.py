
# Création de la classe Forme
class Forme:
    def aire(self):
        return 0

# Création de la classe Rectangle héritant de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=5, hauteur=10)

# Écriture en console du résultat de la méthode aire de la classe Rectangle
print("L'aire du rectangle est:", rectangle.aire())

