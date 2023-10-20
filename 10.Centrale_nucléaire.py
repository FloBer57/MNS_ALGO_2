#Contrôle d'une centrale nucléaire pas la différence de températures.

print("Petit programme pour contrôler la température d'une centrale nucléaire.")

while True :
    try : 
        temp_ambiante = float(input("Veuillez entrer la température ambiante en degré celcius. "))
        break
    except ValueError : 
        print("Veuillez suivre la consigne.")


while True :
    try : 
        temp_bassin = float(input("Veuillez entrer la température du bassin en degré celcius. "))
        break
    except ValueError : 
        print("Veuillez suivre la consigne.")

dif = temp_ambiante - temp_bassin 

if dif > 40 or dif < 20 : 
    print(f"Afficher l'alarme ( La différence est de {dif} )")
else : 
    print(f"Tout vas bien ( La différence est de {dif} )")