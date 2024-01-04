
class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
        
    def ajouter_population(self, nombre):
        self.__population += nombre
        
    def obtenir_population(self):
        return self.__population
    
    def __str__(self):
        return f"Population de la ville de {self.__nom}: {self.__population} habitants"

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        
    def ajouterPopulation(self):
        self.__ville.ajouter_population(1)

# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(paris)
print(marseille)

# Affichage de la population initiale
population_paris_initiale = paris.obtenir_population()
population_marseille_initiale = marseille.obtenir_population()

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)

chloe = Personne("Chloé", 18, marseille)
print("Mise à jour de la", marseille)

# Augmentation de la population suite à l'arrivée des nouvelles personnes
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage de la population après l'ajout des nouvelles personnes
population_paris_finale = paris.obtenir_population()
population_marseille_finale = marseille.obtenir_population()

(population_paris_initiale, population_marseille_initiale,
 population_paris_finale, population_marseille_finale)

print("Mise à jour de la", paris)
print("Mise à jour de la", marseille)


