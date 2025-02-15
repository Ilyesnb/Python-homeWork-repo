#1.Entre un prix HT
Tva= 0.19
while True:
    prix_ht = float(input("entrez un prix HT ( 0 pour terminer) : "))
    if prix_ht== 0:
        break
    prix_ttc = prix_ht*1.19
    print(f"prix ttc: {prix_ttc:.2f}")
somme= 0
count= 0 
sup_100=0
#2.Calcule la somme
while True:
    nombre= float(input("Entre un nombre positif ou nul (<=0 pour terminer) : "))
    if nombre <=0 :
        break
    somme += nombre
    count+= 1
    if nombre > 100:
        sup_100+=1
print(f"Somme totale : {somme}")
print(f"Nombre total D'entrée : {count}")
print(f"Nombre de valeur supérieures a 100 : {sup_100}")
        
    