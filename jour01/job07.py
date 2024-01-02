class Personnage:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x -= 1
    
    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y += 1
    
    def bas(self):
        self.y -= 1
    
    def position(self):
        return (self.x, self.y)
    
personnage_instance = Personnage(0, 0)

personnage_instance.gauche()
personnage_instance.haut()
print(personnage_instance.position())

personnage_instance.droite()
personnage_instance.droite()
personnage_instance.bas()
print(personnage_instance.position())

