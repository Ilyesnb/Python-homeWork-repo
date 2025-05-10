#boucle
i=1
while i< 10 :
    i+=1
print(i)
for i in range (1,10) :
    print(i)
#Triangle
taille = 5
for i in range(1,taille+1):
    print("*"*i)
#Carrés
taille= 5
for i in range(taille):
    print("*"*taille)
#Listes(TABLEAUX)[
MyList= []
fruitList=["apple","banana","blueberyy"]
print(fruitList)
print(f"La liste contient {len(fruitList)} éléments.")
fruitList[1]="watermelon"
print(fruitList)
del fruitList[1]
print(fruitList)
fruitList.append("charyy")
print(fruitList)
# 8.parcourire les elemnts de la liste 
# avec methode for 
NumList =[10,20,16,17,19,15]
for element in NumList :
    print(element)
#avec methode while
i=0
while i<len(NumList) :
    print(NumList[i])
    i+=1
import random
# Générer un nombre aléatoire entre 1 et 100 (inclus)
nombre_aleatoire= random.randint(1,100)
print(f"Nombre aléatoire (randint) : {nombre_aleatoire}")
# Générer un nombre aléatoire entre 1 et 10 avec un pas de 2
nombre_aleatoire=random.randrange(1,10,2)
print(f"Nombre aléatoire (randrange) : {nombre_aleatoire}")
# Sélectionner un élément aléatoire dans la liste
fruit_choice= random.choice(fruitList)
print(f"Fruit choisi (choice) : {fruit_choice}")
random.shuffle(NumList)
print(f"Liste mélangée (shuffle) : {NumList}")  # L'ordre des nombres sera aléatoire
