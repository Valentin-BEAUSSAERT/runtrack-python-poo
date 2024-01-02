class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom 
    
mon_animal = Animal()
print(f"L'âge de l'animal : {mon_animal.age} ans.")

mon_animal.vieillir()
print(f"L'âge de l'animal : {mon_animal.age} ans")

mon_animal.nommer("Luna")
print(f"L'animal se nomme {mon_animal.prenom}")