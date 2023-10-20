#Je demande à l'utilisateur de rentrer les 3 nombres différents pour ma liste.
print("Ce petit programme permet de ranger les nombres par liste croissant")

nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

#Je crée une liste avec les trois nombres.
nombres = [nombre1, nombre2, nombre3]

#.sort() permet de trier la liste. sort(reverse=True) fait en ordre décroissant
# Cependant, cela modifie la liste de base. Pour ne pas modifier, il faut créer une nouvelle liste exemple : ma_nouvelle_liste = sorted(ma_liste).

nombres.sort()

#J'affiche les nombres triées.
print("Les nombres triés dans l'ordre croissant sont :", nombres)