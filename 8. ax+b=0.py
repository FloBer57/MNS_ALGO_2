#Je vais faire un programme permettant de résoudre l'équiation ax + b = 0

print("Nous allons résoudre ax+b = 0")

while True : 
    try : 
        a = float(input("Veuillez rentrer la valeur de A en nombre réel. "))
        break
    except ValueError : 
        print("Veuillez suivre la consigne donné pour la valeur de A ")

while True : 
    try : 
        b = float(input("Veuillez rentrer la valeur de B en nombre réel. "))
        break
    except ValueError : 
        print("Veuillez suivre la consigne donné pour la valeur de B ")

while True : 
    try : 
        x = float(input("Veuillez rentrer la valeur de X en nombre réel. "))
        break
    except ValueError : 
        print("Veuillez suivre la consigne donné pour la valeur de X ")

if a == 0 and b == 0 : 
    print(f"la solution pour ({a}*{x})+{b} = 0 est l'ensemble R")
elif a == 0 and b != 0 : 
    print(f"la solution pour ({a}*{x})+{b} = 0 est l'ensemble vide")
elif a != 0 :
    sol = -b/a
    print(f"la solution pour {a} n'est pas égale à 0 et est donc {sol} ( soit l'opération étant {-b}/{a} )")