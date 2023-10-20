import sys

list = ["oui","non"]
list2 = ['café','thé','chocolat chaud']

print("The Frienship Algorithm. Première étape, passez un appel. ")

while True : 
    try :
        home = str(input("Est-il à la maison? Repondez par oui ou par non ( minuscule ) "))
        if home in list : 
            break
    except ValueError :
        print("Suivez la consigne")

# Home?

if home == "oui" :
    while True : 
        try :
            meal = str(input("Dites lui 'Aimerai tu que l'on partage un repas?' Qu'à t-il dit? Repondez par oui ou par non ( minuscule ) "))
            if meal in list : 
                break
        except ValueError :
            print("Suivez la consigne")
else : 
    while True : 
        try :
            meal = str(input("Laissez un message, attendez qu'il vous rappel et proposez lui 'Aimerai tu que l'on partage un repas?' Qu'à t-il répondu? Repondez par oui ou par non ( minuscule ) "))
            if meal in list : 
                break
        except ValueError :
            print("Suivez la consigne")

# What is the reponse? 

if meal == "oui" : 
    print("Dinez ensemble et félicitation, vous êtes amis! ")
    sys.exit("Fin du programme") 
else : 
    while True : 
        try :
            beverage = str(input("S'il à répondu non, dites lui 'Est-ce que ça te plairait d'aller boire une boisson chaude? Qu'à t-il répondu? Repondez par oui ou par non ( minuscule ) "))
            if beverage in list : 
                break
        except ValueError :
            print("Suivez la consigne")
# Boisson chaude

if beverage == "oui" :
    while True : 
        try :
            drink = str(input("Superbe! Vous préférez un café, un thé ou un chocolat chaud? Choisissez en recopiant avec la même ortographe. ( en minuscule ) "))
            if drink in list2 : 
                print("Félicitation! Vous êtes devenu ami !")
                sys.exit("Fin du programme") 
        except ValueError :
            print("Suivez la consigne")
else : 
    while True : 
        try :
            recre = str(input("N = 0, Demandez lui quelle est son activité préféré? Partage t-il cette info? Repondez par oui ou par non ( minuscule ) "))
            if recre in list : 
                break
        except ValueError :
            print("Suivez la consigne")

# Recreationnal

share = 'o'
test = 0

while share != "oui" : 
    if recre == "oui" : 
        print("'Super! Dites lui 'Est-ce qu'on pourrait pas faire ça ensemble?' Faites le, et FELICITATION, vous êtes devenu ami !")
        sys.exit("Fin du programme") 
    else : 
        while True :  
            try :
                test = test +1
                share = str(input(f"N = N+1 .  N est-il supérieur à 6? Il est actuellement à {test} ? Repondez par oui ou par non ( minuscule ) "))
                if share in list : 
                    break
            except ValueError :
                print("Suivez la consigne") 

    # What is the reponse of n>6

    if share == "oui" :
            print("Super! Choisissez un intéret objectionnel et dites le, et FELICITATION, vous êtes devenu ami !")
            sys.exit("Fin du programme") 

