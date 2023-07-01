"""
Les structure conditionelle
"""

a = int(input('Nous voulon un nombre >'))
b = int(input('Nous voulon un nombre >'))
c = int(input('Nous voulon un nombre >'))

if a>0 and b>0 and c>0:#Expression booleen
    print("Tout les nombres sont positif et superieure a zero")

    #Le if simple

if a==0:
    print("Le premier est egale a zero")
else:
    print("Le premier n'est pas egale a zero")

    #Le if else

if a>b and a>c:
    print("Le premier est le plus grand")
elif b>a and b>c:
    print("Le deuxieme est le plus grand")
elif c>a and c>b:
    print("Le troisieme est le plus grand")
else:
    print("Ils sont tous egaux")

    #Le if elif else
