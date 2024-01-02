class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT + (self.prixHT * self.TVA / 100)
    
    def afficher(self):
        return (self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC())
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom 
    
    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    def getnom(self):
        return self.nom 
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA
    
produit1 = Produit("Produit 1", 100, 20)  # Un produit avec un prix HT de 100 et 20% de TVA
produit2 = Produit("Produit 2", 200, 10)

#Afficher les informations des produits 
infos_produit1 = produit1.afficher()
infos_produit2 = produit2.afficher()

# Modifions le nom et le prix HT de chaque produit
produit1.modifierNom("Produit 1 Nouveau")
produit1.modifierPrixHT(150)

produit2.modifierNom("Produit 2 Nouveau")
produit2.modifierPrixHT(250)

# Affichons de nouveau les informations des produits après les modifications
infos_produit1_modifie = produit1.afficher()
infos_produit2_modifie = produit2.afficher()

(infos_produit1, infos_produit2, infos_produit1_modifie, infos_produit2_modifie)


#print(infos_produit1_modifie)  # Ajout de l'impression des informations
#print(infos_produit2_modifie)