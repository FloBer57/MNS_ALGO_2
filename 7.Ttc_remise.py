#Petit programme pour appliquer une remise selon des conditions.

print("Petit programme permettant de vous calculer une remise.")

#Je demande à ce que il ne sois pris en compte que les "float" = nombre réel. Sinon ça renvoi aux phrases d'avant. 

while True :
    try:
        prix_ttc = float(input("Veuillez rentrer un prix en Euros : "))
        break
    except ValueError : 
        print("Veuillez bien rentrer un prix en Euros en chiffre réel.")

#Je demande à ce qu'en fonction du prix il applique une certaine remise suivant l'exercice. 

if 500 <= prix_ttc <= 1000 :
    remise = prix_ttc * 0.98
    print(f"Le prix de {prix_ttc} permet d'obtenir une remise de 2%, qui nous donnent {remise}.")
elif 1000 < prix_ttc <= 2000 :
    remise = prix_ttc * 0.95
    print(f"Le prix de {prix_ttc} permet d'obtenir une remise de 5%, qui nous donnent {remise}.")
elif 2000 < prix_ttc :
    remise = prix_ttc * 0.90
    print(f"Le prix de {prix_ttc} permet d'obtenir une remise de 10%, qui nous donnent {remise}.")
else :
    print(f"Le prix qui est {prix_ttc} est inférieur à 500 euros, vous ne pouvez pas obtenir de remise.")