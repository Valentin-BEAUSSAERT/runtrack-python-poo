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

# Redéfinition de la classe Professeur pour ajouter un âge au professeur
        
class Professeur:
    def __init__(self, matiere_enseignee, age=40):
        self.__matiere_enseignee = matiere_enseignee
        self.__age = age

    def enseigner(self):
        print("Le cours va commencer")
    
    def bonjour(self):
        print('Hello')

    def afficherAge(self):
        print(f"Le professeur a {self.__age} ans.")

# Instanciation d'un élève et exécution des actions demandées
eleve = Eleve()
eleve.bonjour()  # L'élève dit bonjour
eleve.allerEnCours()  # L'élève annonce qu'il va en cours
eleve.modifierAge(15)  # L'âge de l'élève est mis à 15 ans
eleve.afficherAge()  # Affiche le nouvel âge de l'élève

# Instanciation d'un professeur et exécution des actions demandées
professeur = Professeur(matiere_enseignee="Mathématiques", age=40)
professeur.bonjour()  # Le professeur dit bonjour
professeur.enseigner()  # Le professeur annonce que le cours va commencer
professeur.afficherAge()  # Affiche l'âge du professeur (utilisé pour vérification)


