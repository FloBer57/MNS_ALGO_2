mot = str(input("Veuillez rentrer un mot en minuscule"))
nb_lettres = 0

for i in range (0,len(mot)) :
    nb_lettres = nb_lettres + 1

print(f"nombres de lettres = {nb_lettres}")

nb_lettres = nb_lettres/2
variable_plus = 0
variable_moins = 0

while variable_plus < nb_lettres : 
    if mot[variable_plus] == mot[variable_moins] :
        variable_plus = variable_plus + 1 
        if variable_plus < nb_lettres :
            True
        else :
            print("c'est un palindrôme")
            break
    else:
        print(" ce n'est pas un palindrôme")

