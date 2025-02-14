#1.definir un tableau
tab=[7,3,7,9,7,13,15]
print("tableau : ",tab)
#2.Calcule la moyenne
def calculer_moyenne(liste):
    if(liste)==0:
        return 0
    else:
        return sum(liste)/ len(liste)
moyenne= calculer_moyenne(tab)
print("la moyenne est : ",moyenne)
#3 Nombre d'occurrences 
def compter_occurence (tab,element):
    return tab.count(element)
element_a_cherche = 7
print(f"le nombre {element_a_cherche} apparait",compter_occurence(tab,element_a_cherche),"fois")
#4 Elemnt superieurs a 10
def compter_superieurs_a_10(tab):
    compteur = 0
    for number in tab:
        if number>=10:
            compteur+=1
    return compteur
resultat = compter_superieurs_a_10(tab)
print("Nombre d'element superieurs a 10 :",resultat)      
#5 valeur maximale du ta    bleau
def valeur_maximale(tab):
    if not tab:
        return None
    max_val=tab[0]
    for nomber in tab : 
        if nomber > max_val:
            max_val=nomber
    return max_val
resultat = valeur_maximale(tab)
print("valeur maximale du tableau :", resultat)
#6 element present
def element_present(tab,elemnt):
    return elemnt in tab
element_a_verifier= 9
print(f"l'element {element_a_verifier} est present :", element_present(tab,element_a_verifier))
#8 tableau n entiers aléatoires
import random
def randomTab(n):
    tableau = []
    for _ in range (n):
        nombre = random.randint(1,100)
        tableau.append(nombre)
    return tableau
n=10
randomTabGenerateur= randomTab(n)
print("Tableau aleatoire :",randomTabGenerateur )
#9 entiers melanges aleatoirement
def RandomMix (n):
    tableau = list(range(1,n+1))
    random.shuffle(tableau)
    return tableau
n=10
MixTab = RandomMix(n)
print("tableau melangé : ", MixTab)        