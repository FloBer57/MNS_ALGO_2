#Calcul de moyenne des notes d'un élève après avoir saisi différentes notes ainsi que leurs Coeff

print("Ceci permet de calculer la moyenne des notes d'un élève.")

#Création des variables des notes et des coefficients

note_français = float(input("Veuillez rentrer la note de français (/20) "))
note_math = float(input("Veuillez rentrer la note de math (/20) "))
note_geo = float(input("Veuillez rentrer la note de geo (/20) "))
note_info = float(input("Veuillez rentrer la note d'informatique (/20) "))

coeff_français = int(input("Veuillez rentrer le coefficient de français "))
coeff_math = int(input("Veuillez rentrer le coefficient de math "))
coeff_geo = int(input("Veuillez rentrer le coefficient de geo "))
coeff_info = int(input("Veuillez rentrer le coefficient d'informatique "))

#Création des calculs de moyennes
moyenne_fr = note_français * coeff_français
moyenne_math = note_math * coeff_math
moyenne_geo = note_geo * coeff_geo
moyenne_info = note_info * coeff_info

#Calculs finaux
coeff_globable = coeff_français + coeff_math + coeff_geo + coeff_info 
moyenne_globable = ( moyenne_fr + moyenne_math + moyenne_geo + moyenne_info ) / coeff_globable

#Utilisation du ROUND(valeurs,2) le 2 étant le nombre de chiffre après la virgule voulu ( Pour éviter d'avoir un chiffre à rallonge )

print(f"La moyenne d'un élève ayant {note_français} en français, {note_math} en math, {note_geo} en géographie et {note_info} en informatique et de {round(moyenne_globable,2)}. Les coefficients ont été respectées. ")
