class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom 
        
    def sePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "Jean")

print(personne1.sePresenter())
print(personne2.sePresenter())

    