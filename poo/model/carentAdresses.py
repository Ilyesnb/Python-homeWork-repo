class Personne : 
    def __init__(self,nom,prenom,telephone="inconnu"):
        self.nom = nom 
        self.prenom = prenom
        self.telephone = telephone
class CarnetAdresses :
    def __init__(self) :
        self.contacts = []
    def ajouter_contact(self,personne):
        self.contacts.append(personne)
    def chercher_contact (self,nom,prenom = None):
        for contact in self.contacts:
            if contact.nom == nom :  
              if prenom is None or contact.prenom == prenom :
                print(f"{contact.nom},{contact.prenom} -- Téléphone : {contact.telephone}") 
# Exemple d'utilisation
carnet = CarnetAdresses()
carnet.ajouter_contact(Personne("Ben Salem","Ali","0542565013"))        
carnet.ajouter_contact(Personne("Ben Salem","sana","0671953952"))
print("Recherche de 'Ben Salem' :")
carnet.chercher_contact("Ben Salem")
print("\nRecherche de 'Ben Salem Ali' :")
carnet.chercher_contact("Ben Salem","Ali")
        