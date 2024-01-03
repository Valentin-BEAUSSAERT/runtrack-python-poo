# Adding print statements to display all the information about the book at each step.

class Livre:
    def __init__(self, titre, auteur, nbrPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrPages = nbrPages
        self.__disponible = True 
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        print(f"Le titre du livre a été mis à jour : {self.__titre}")
    
    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur
        print(f"L'auteur du livre a été mis à jour : {self.__auteur}")
    
    def get_nbrPages(self):
        return self.__nbrPages
    
    def set_nbrPages(self, nbrPages):
        if isinstance(nbrPages, int) and nbrPages > 0:
            self.__nbrPages = nbrPages
            print(f"Le nombre de pages a été mis à jour : {self.__nbrPages}")
        else:
            print("Erreur, le nombre de pages doit être un entier positif")
    
    def verification(self):
        disponibilite = "disponible" if self.__disponible else "indisponible"
        print(f"Vérification de la disponibilité: Le livre est {disponibilite}")
        return self.__disponible 
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est actuellement pas disponible")
    
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'était pas emprunté")
    
    def __str__(self):
        disponibilite = "Disponible" if self.__disponible else "Indisponible"
        return f"Livre (Titre :{self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nbrPages}, Disponibilité : {disponibilite})"
    
# Création d'un objet Livre
livre = Livre("Les Misérables", "Victor Hugo", 500)
print(livre)  # Initial state

# Vérification de la disponibilité avant l'emprunt
disponible_avant = livre.verification()

# Emprunter le livre
livre.emprunter()

# Vérification de la disponibilité après l'emprunt
disponible_apres_emprunt = livre.verification()

# Rendre le livre
livre.rendre()

# Vérification de la disponibilité après le retour
disponible_apres_retour = livre.verification()

# Mise à jour du nombre de pages à un entier positif
livre.set_nbrPages(300)

# Tentative de mise à jour du nombre de pages avec une valeur invalide (négative)
livre.set_nbrPages(-10)  # Ceci va imprimer le message d'erreur

# Afficher l'état final du livre
etat_final = livre.__str__()
print(etat_final)
