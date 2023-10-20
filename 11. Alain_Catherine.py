# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.

print("Petit programme permettant de savoir qui sera invité à la soirée.")

liste = [0,1]

while True :
    try :
        ami_alain = int(input("Veuillez rentrez 1 si vous avez comme ami alain, 0 si vous ne l'êtes pas."))
        if ami_alain in liste :
            break
    except ValueError : 
        print("Veuillez rentrer un chiffre, 0 ou 1.")

while True :
    try :
        joue_bridge = int(input("Veuillez rentrez 1 si vous jouez au bridge, 0 si vous n'y jouais pas."))
        if joue_bridge in liste :
            break
    except ValueError : 
        print("Veuillez rentrer un chiffre, 0 ou 1.")

while True :
    try :
        ami_catherine = int(input("Veuillez rentrez 1 si vous avez avez comme ami catherine, 0 si vous ne l'êtes pas."))
        if ami_catherine in liste :
            break
    except ValueError : 
        print("Veuillez rentrer un chiffre, 0 ou 1.")
        

if ami_catherine == 1 and ami_alain == 1 :
    print("Vous pouvez venir à la soirée.")
elif ami_catherine == 1 and  ami_alain == 0 : 
    print("Vous pouvez venir à la soirée.")
elif joue_bridge == 1 and ami_catherine == 0 : 
    print("Vous pouvez venir à la soirée.")
else : 
    print("Perdu")