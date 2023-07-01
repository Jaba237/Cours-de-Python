"""
Chiffres en colonne
1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5
"""

n = int(input("Entrer le nombre de lignes >"))

if n<=0 :
    print("Le nombre est mauvais")
else :
    for i in range(n):
        for k in range(i+1):
            print(k+1,end=' ')
        print('\n')
#Vous aller remarquer le end=' ' ceci veu dire que ma chaine fini avec un espece
#La fonction in prend troi parametre de passe le premier est l'objet
#le deuxieme c'est le separateur
#et apres on a le caractere de fin
