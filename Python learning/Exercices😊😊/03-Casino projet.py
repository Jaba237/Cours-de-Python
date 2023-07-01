"""
Super Casino app de la roulette

"""
import random
import math

print("Bienvenu dans le super jeu de la roullette")

print('\n')

mise = int(input("Entrer votre mise >"))

while mise<=1:
    mise = int(input("Entrer une bonne mise soyer pas peureux >"))
    print('\n')
chiffre = int(input("Entrer votre chiffre de 0 a 49 >"))
print('\n')

while chiffre<0 or chiffre>=50:
    chiffre = int(input("Entrer un bon chiffre"))

print('C\'est partie')

vrai = True
gain = 0

while vrai:
    nbr = random.randrange(50)

    if nbr == chiffre:
        gain = 3*mise
    elif nbr%2 == chiffre%2:
        mise = math.ceil(mise/2)
    else:
        mise = 0

    print("Votre gain actuelle ",gain)
    if mise!=0:
        print("Vous recuperer ",mise)

    print("Voulais vous encore mise ? o/n")

    volonte = str(input())

    if volonte == 'o':
        mise = int(input("Entrer votre mise >"))

        while mise<=1:
            mise = int(input("Entrer une bonne mise soyer pas peureux >"))
            print('\n')
        chiffre = int(input("Entrer votre chiffre de 0 a 49 >"))
        print('\n')

        while chiffre<0 or chiffre>=50:
            chiffre = int(input("Entrer un bon chiffre"))

        print('C\'est partie')
        vrai = True
    else:
        print("C'etait une partie de plaisir")

        print("Vous avez gagner ",gain)

        vrai = False

    
