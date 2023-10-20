#[ALGO] Exercice  : Taux d’intérêt

#Jean a un livret A avec 2000 euros dessus au taux d’intérêt de 2%
#- Ecrire un programme pour savoir combien il aura dans 10 ans
#- Modifier le programme pour pouvoir choisir le taux d’intérêt et le nombre d’années


somme = 2000


while True : 
    try :
        année = int(input("Veuillez rentrer le nombre d'année "))
        break
    except ValueError :
        ("Veuillez suivre la consigne ")

while True : 
    try :
        taux = float(input("Veuillez rentrer le taux d'intêret comme suit : XX "))
        break
    except ValueError :
        ("Veuillez suivre la consigne ")


taux = taux/100 + 1

print(taux)

for i in range (0,année) :
    somme = somme * taux
    print(round(somme))

dif = somme - 2000

print(f"Si vous placez 2000 euros, dans {année}, vous aurez {dif(somme)}, soit {round(dif)} de plus.")