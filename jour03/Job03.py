
class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = 'à faire' 

    def marquer_comme_finie(self):
        self.statut = 'terminé'  

    def __str__(self):
        return f"{self.titre} ({self.description}) - {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = [] 
    def ajouter_tache(self, tache):
        self.taches.append(tache) 

    def supprimer_tache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]  

    def afficher_liste(self):
        return "\n".join(str(tache) for tache in self.taches) 

    def filtrer_liste(self, statut):
        return "\n".join(str(tache) for tache in self.taches if tache.statut == statut) 

    def marquer_toutes_comme_finies(self):
        for tache in self.taches:
            tache.marquer_comme_finie() 
liste_de_taches = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter du lait, des œufs et du pain")
tache2 = Tache("Réparer la porte", "Changer les charnières de la porte de la chambre")

liste_de_taches.ajouter_tache(tache1)
liste_de_taches.ajouter_tache(tache2)

print("Liste des tâches:")
print(liste_de_taches.afficher_liste())

tache1.marquer_comme_finie()
print("\nListe des tâches après mise à jour:")
print(liste_de_taches.afficher_liste())

liste_de_taches.marquer_toutes_comme_finies()
print("\nListe des tâches terminées:")
print(liste_de_taches.filtrer_liste('terminé'))
