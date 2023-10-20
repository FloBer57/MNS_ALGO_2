# En athlétisme, les coureurs sont répartis suivant les
# classes d'âge suivantes : 
# Eveil : avant 10 ans 
# Poussin: de 10 à 11 ans 
# Benjamin: de 12 à 13 ans 
# Minime: de 14 à 15 ans 
# Cadet: de 16 à 17 ans 
# Junior: de 18 à 19 ans 
# Espoir: de 20 à 22 ans 
# Senior: de 23 à 39 ans 
# Vétéran : 40 et plus 

# a) Écrire un algorithme qui :
# - demande à l’utilisateur son âge, 
# - et l’informe de sa catégorie. 

# b) Écrire un algorithme qui :
# - demande à l’utilisateur son âge, 
# - et l’informe s'il est ou non Benjamin.# 

import datetime

date_actuelle = datetime.date.today()

print("Nous sommes le ",(date_actuelle)," veuillez rentrer votre date de naissance comme cité par la suite" )

list_year = [i for i in range(1900, 2024)]
list_month = [i for i in range(1, 13)]
list_day = [i for i in range(1, 32)]
#Je demande de rentrer les valeurs année/mois/jours
while True :
    try : 
        year_birth = int(input("Veuillez rentrer l'année de votre naissance au format (AAAA) "))
        if year_birth in list_year :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")

while True :
    try : 
        month_birth = int(input("Veuillez rentrer le mois de votre naissance au format (MM) "))
        if month_birth in list_month :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")

while True :
    try : 
        day_birth = int(input("Veuillez rentrer le jour de votre naissance au format (JJ) "))
        if day_birth in list_day :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")        


age = date_actuelle.year - year_birth - ((date_actuelle.month, date_actuelle.day) < (month_birth, day_birth))



if age < 10 :
    print(f"Vous êtes dans la catégorie Eveil ( avant 10 ans ) car vous avez {age} ans")
elif 10 >= age < 12 :
    print(f"Vous êtes dans la catégorie Poussin ( 10 à 11 ans  ) car vous avez {age} ans")
elif 12 >= age < 14 :
    print(f"Vous êtes dans la catégorie Benjamin ( 12 à 13 ans  ) car vous avez {age} ans")
elif 14 >= age < 16 :
    print(f"Vous êtes dans la catégorie Minime ( 14 à 15 ans  ) car vous avez {age} ans")
elif 16 >= age < 18 :
    print(f"Vous êtes dans la catégorie Cadet ( 16 à 17 ans  ) car vous avez {age} ans")
elif 18 >= age < 20 :
    print(f"Vous êtes dans la catégorie Junior ( 18 à 19 ans  ) car vous avez {age} ans")
elif 20 >= age < 23 :
    print(f"Vous êtes dans la catégorie Espoir ( 20 à 22 ans  ) car vous avez {age} ans")
elif 23 >= age < 40 :
    print(f"Vous êtes dans la catégorie Senior ( 23 à 39 ans ) car vous avez {age} ans")
elif age >= 40 :
    print(f"Vous êtes dans la catégorie Vétéran ( 40 et plus  ) car vous avez {age} ans")
if 12 < age > 14 : 
    print(f" Vous n'êtes pas benjamin car vous avez {age} ans")