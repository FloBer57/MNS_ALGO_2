#Petit programme permettant de savoir si un enfant à le droit d'avoir une palette ou pas ( Il peut la recevoir s'il à moins de 3 ans)

# Je récupère la date du jour par un import datetime, date_actuelle la récupère.
import datetime

date_actuelle = datetime.date.today()

print("Nous sommes le ",(date_actuelle)," veuillez rentrer la date de naissance de votre enfant comme cité par la suite" )

#Je demande de rentrer les valeurs année/mois/jours

year_birth = int(input("Veuillez rentrer l'année de naissance de votre enfant au format (AAAA) "))
month_birth = int(input("Veuillez rentrer le mois de naissance de votre enfant au format (MM) "))
day_birth = int(input("Veuillez rentrer le jour de naissance de votre enfant au format (JJ) "))

# Je demande l'âge limite donc se sera 3.

age_limit = 3

# Age de l'enfant = année actuelle - année de l'enfant - (( compare le mois et le jour actuel au mois et jour de naissance de l'enfant.))

age_enfant = date_actuelle.year - year_birth - ((date_actuelle.month, date_actuelle.day) < (month_birth, day_birth))

# Si age enfant < 3, alors blablabla

if age_enfant < age_limit :
    print("Votre enfant peux obtenir un petit pot car il à moins de 3 ans, félicitation")
else : print(f"Votre enfant ne peux pas recevoir de petit pot car il à plus que {3} ans")

