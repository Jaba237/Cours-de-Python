"""
Les boucles en python
On a la boucle defini
for
Et la boucle indefini
while
"""



#Utilison le while pour calcul le factoriel


n = int(input('Entrer un nombre entier >'))

while n<0:
    print("Entrer un bon nombre")
    n = int(input('Entrer un nombre entier >'))

if n==0 or n==1:
    print("Le factoriel est >",1)
else:
    i = 1
    fact = 1
    while i<=n:
        fact = fact * i
        i+=1
print("Le factoriel est >",fact)
