

class Point:
    def __init__(self, x, y):           #Constructeur de la classe avec 2 paramètres, x et y, qui sont les coordoonées du point 
        self.x = x                      #Attribut public x
        self.y = y                      #Attribut public y
    
#Méthode pour affciher les coordonnées du point 
    def afficherLesPoints(self):
        print(f"Les coordoonées des points sont : ({self.x}, {self.y})")
#Méthode pour afficher la coordonnée x du point
    def afficherX(self):
        print(f"La position du point x est : {self.x}")
#Méthode pour afficher la coordonnée y du point
    def afficherY(self):
        print(f"La position du point x est : {self.y}")
#Méthode pour changer la valeur de la coordonnée x
    def changerX(self, nouveau_X):
        self.x = nouveau_X
#Méthode pour changer la valeur de la coordonnée y
    def changerY(self, nouveau_Y):
        self.y = nouveau_Y

#Création d'une instance de la classe Point avec les coordonnées x=2 et y=3
p = Point(2, 3)
#Affichage des coordonnées du point p
p.afficherLesPoints()
#Affichage de la coordonnée x du point p
p.afficherX()
#Affichage de la coordonnée y du point p
p.afficherY()
#Changement de la coordonnée x en 5 pour le point p
p.changerX(5)
#Changement de la coordonnée y en 8 pour le point p 
p.changerY(8)
#Affichage des nouvelles coordonnées du point p après modification
p.afficherLesPoints()
#Affichage de la nouvelle position x du point p
p.afficherX()
#Affichage de la nouvelle position y du point p
p.afficherY()