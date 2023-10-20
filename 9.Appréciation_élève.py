#Ci-joint un petit programme pour obtenir immédiatement l'appréciation d'un élève en fonction de sa note. 

print("Petit programme permettant d'obtenir une appréciation d'un élève en fonction de sa moyenne.")

#Je me crée une liste de notes possible à pouvoir rentrer dans mon code. Les autres valeurs ne seront pas acceptées. 

notes_valides = list(range(21))

#Dans la liste de range 21, il y a tout les nombre possible entre 0 et 20 ( 0 exclu, d'ou le append qui est une fonction qui permet d'ajouter dans une liste des éléments. )
notes_valides.append(0)

while True : 
    try : 
        note_fr = float(input("Veuillez rentrer la note de français/20 "))
        note_math = float(input("Veuillez rentrer la note de mathématiques/20 "))
        note_geo = float(input("Veuillez rentrer la note de géographie/20 "))
        note_info = float(input("Veuillez rentrer la note de informatique/20 "))

        #Cela permet de vérifier si toutes les notes sont valide. On aurait pu refaire à chaque fois pour vérifier à chaque input ( Possible erreur de ma part 
        # )
        if (note_fr and note_math and note_geo and note_info) in notes_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 0 et 20 pour chaqu'une des notes. ")
    except ValueError : 
        print("Veuillez bien rentrer un nombre entre 0 et 20 ")

moyenne_eleve = ( note_fr + note_math + note_geo + note_info ) / 4

if 20 >= moyenne_eleve >= 16 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Très bien.>>")
elif 16 > moyenne_eleve >= 12 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Bien.>>")
elif 12 > moyenne_eleve >= 8 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Assez bien.>>")
elif 8 > moyenne_eleve >= 4 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Insufisant.>>")
elif 4 > moyenne_eleve >= 0 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Nul.>>")