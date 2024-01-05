# Définition de la classe Personne en Python
class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans.")

    def bonjour(self):
        print('Hello')

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

# Définition de la classe Eleve qui hérite de Personne
class Eleve(Personne):
    # Pas besoin de redéfinir le constructeur si on n'ajoute pas d'attributs

    def allerEnCours(self):
        print("Je vais en cours")

    # Redéfinition de la méthode afficherAge
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

# Définition de la classe Professeur
class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une Personne et d'un Eleve
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()  # Cela doit afficher "J'ai 14 ans."

