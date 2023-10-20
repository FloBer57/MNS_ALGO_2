#Petit programme pour permettre d'avoir le prix en fonction d'une TVA différente.

print("Petit programme permettant de calculer votre prix total.")

while True :
    try:
        prix_ht = float(input("Veuillez rentrer le prix HT d'un produit ( en Euros ) "))
        break
    except ValueError :
        print("Veuillez rentrer un nombre réel en Euros valide.")    


while True : 
    try:
        choix = int(input("Veuillez rentrer le chiffre 1 pour une TVA de 5.5%, le chiffre 2 pour une TVA de 19.5%, le chiffre 3 pour une TVA de 33%."))
        if choix in [1,2,3]:
            break
    except ValueError :
        print("Veuillez rentrer un chiffre entre 1,2 et 3.")



TVA5p5 = 1.055
TVA19p5 = 1.195
TVA33 = 1.33

if choix == 1:
    TTC_5p5 = prix_ht * TVA5p5
    print(f"Le prix HT est de {prix_ht}, la TVA est de 5.5% et le prix TTC est de {TTC_5p5} ")

elif choix == 2:
    TTC_19p5 = prix_ht * TVA19p5
    print(f"Le prix HT est de {prix_ht}, la TVA est de 19.6% et le prix TTC est de {TTC_19p5} ")

elif choix == 3:
    TTC_33 = prix_ht * TVA33
    print(f"Le prix HT est de {prix_ht}, la TVA est de 33% et le prix TTC est de {TTC_33} ")
