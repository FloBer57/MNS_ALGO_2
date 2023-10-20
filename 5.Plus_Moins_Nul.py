#Petit programme permettant de savoir si le chiffre en INPUT est Positif, Nul ou Négatif.

print("Permet de savoir si un chiffre est positif, nul ou négatif.")

while True:
    # While c'est tant que VRAI. Ceci est symbolisé par le TRY. Le TRY ici permet de vérifier que la valeur rentré par l'utilisateur ( qui est donc de base en String vu que c'est une chaine de caractèr ) est "convertissable" en FLOAT. S'il l'est, alors try renvoi un TRUE donc ça continue. Sinon, except 
    try:
        nombre = float(input("Veuillez rentrer un nombre réel : "))
        break  # Sort de la boucle si la conversion en float réussit

    # Dans cet exemple, nous utilisons le bloc except pour afficher un message d'erreur à l'utilisateur, lui indiquant qu'il doit entrer un nombre réel valide, et ensuite la boucle while continue pour lui permettre de réessayer.
    except ValueError:
        print("Erreur : Veuillez entrer un nombre réel valide.")

#Je demande si supérieur à 0 donc positif, inférieur à 0 donc négatif, sinon nul.

if nombre > 0 :
    print(f"Le nombre {nombre} est positif")
elif nombre < 0 : 
    print(f"Le nombre {nombre} est négatif")
else :
    print(f"Le nombre {nombre} est nul")