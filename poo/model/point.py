class Point :
    def __init__(self,x=3.0,y=4.0) :
        self.x =x
        self.y = y
    def afficher (self) :
        print (f"Point({self.x},{self.y})")
class Rectangle :
    def __init__(self,coin,largeur,hauteur):
        self.coin = coin
        self.largeur = largeur
        self.hauteur = hauteur
    def afficher (self) :
        print(f"Rectongle Coin supérieur gauche ({self.coin.x},{self.coin.y}),"f"Largeur = {self.largeur}, hauteur = {self.hauteur}")
    def modifier_taille(self,nouvelle_largeur,nouvelle_hauteur):
        self.largeur = nouvelle_largeur
        self.hauteur = nouvelle_hauteur
   # Définition de la fonction après la classe Rectangle
def trouverCentre(rectangle):
    """Retourne le centre du rectangle sous forme d'un Point"""
    centre_x = rectangle.coin.x + rectangle.largeur / 2
    centre_y = rectangle.coin.y + rectangle.hauteur / 2
    return Point(centre_x, centre_y)


# 2. Création de l'instance p1 de la classe Point
p1 = Point()

# 3. Affichage du point p1
p1.afficher()

# 5. Création de l'instance boîte de la classe Rectangle
boite = Rectangle(Point(12.0, 27.0), 50.0, 35.0)

# 6. Trouver et afficher le centre du rectangle boîte
centre = trouverCentre(boite)
print("Centre du rectangle :")
centre.afficher()

# 8. Modifier la taille de l'objet boîte sans modifier sa position
boite.modifier_taille(60.0, 40.0)
boite.afficher()
     