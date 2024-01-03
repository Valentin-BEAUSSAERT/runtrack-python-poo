class Livre:
    def __init__(self, titre, auteur, nbrPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrPages = nbrPages
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur 
    
    def get_nbrPages(self):
        return self.__nbrPages
    
    def set_nbrPages(self, nbrPages):
        if isinstance(nbrPages, int) and nbrPages >0:
            self.__nbrPages = nbrPages
        else:
            print("Erreur, le nombre de pages doit être un entier positif")
    
    def __str__(self):
        return f"Livre (Titre :{self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nbrPages})"
    
# Création d'un objet Livre
livre = Livre("Les Misérables", "Victor Hugo", 500)

# Tentative de définir le nombre de pages à un entier positif
livre.set_nbrPages(300)

# Tentative de définir le nombre de pages à une valeur invalide (entier négatif)
livre.set_nbrPages(-10)  # Ceci va imprimer le message d'erreur

# L'état actuel du livre
etat_actuel = str(livre)

print(etat_actuel)