

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Les coordoonées des points sont : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La position du point x est : {self.x}")

    def afficherY(self):
        print(f"La position du point x est : {self.y}")

    def changerX(self, nouveau_X):
        self.x = nouveau_X

    def changerY(self, nouveau_Y):
        self.y = nouveau_Y

p = Point(2, 3)
p.afficherLesPoints()
p.afficherX()
p.afficherY()

p.changerX(5)
p.changerY(8)

p.afficherLesPoints()
p.afficherX()
p.afficherY()