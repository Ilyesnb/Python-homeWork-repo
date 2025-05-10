class CompteBancaire :
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte = numeroCompte
        self.nom = nom 
        self.solde = solde
    def versement (self,montant) :
        if montant >0 :
            self.solde += montant
            print(f"Versement de {montant} effectué. Nouveau solde :{self.solde} DA")
        else : 
            print("le montant du versement doit etre positif")
    def Retrait(self,montant) :
        if 0< montant<= self.solde:
            self.solde -=montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self.solde}")
        else :
            print("fonds insuffiseants ou montant invalide")
    def Agios (self):
        agios = self.solde*0.05
        self.solde = agios
        print(f"Agois de 5% appliqué ({agios} DA). Nouveau solde : {self.solde} DA")
    def afficher (self) :
        print(f"compte N° : {self.numeroCompte}")
        print(f"Propriétaire : {self.nom}")
        print(f"Solde : {self.solde} DA")
compte = CompteBancaire(123456,"ilyes nabi",10000)
compte.versement(500) 
compte.Retrait(1500)
compte.Agios()
compte.afficher()
