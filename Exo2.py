#Afficher un nombre
print(15)
#Affiche une chaine de caractéres
print("hello world")
#Affiche une variable
message = "ceci est un test"
print(message)
#2.Passer ou ne pas passer a la ligne
print("hello",end=" ")
print("world")
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
#8.