# Petit programme d'un jeu entre 2 joueurs. Si la somme est paire, A est gagnant, sinon B est gagnant.

print("Petit jeu de doigts entre 2 joueurs.")

#Je demande le nombre de doigts de chacun des jouers
while True : 
    try :
        doigt_joueur_A = int(input("Veuillez rentrer le nombre de doigts du joueur A "))
        doigt_joueur_B = int(input("Veuillez rentrer le nombre de doigts du joueur B "))
        break
    except ValueError: 
        print("Veuillez rentrer un nombre valide de doigts")

#Je les additionnes puis je calcule le modulo de la somme par un % (de 2 afin d'obtenir l'information pour pair)

somme_2_joueurs = doigt_joueur_A + doigt_joueur_B
modulo_somme = somme_2_joueurs % 2 

#Puis je demande si le modulo = 0 alors le résultat est forcément paire. Sinon, il est impair.

if modulo_somme == 0:
    print(f"La somme étant {somme_2_joueurs}, le joueur A à gagné")
else : 
    print(f"La somme étant {somme_2_joueurs}, le joueur B à gagné")