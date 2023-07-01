"""
Les constante et fonction mathematique
"""
import math

#Il est primordiale d'importer ce module afin de pouvoir s'en servir

print(math.pi,' ',math.tau,' ',math.e)

#Pour afficher pi tau et la constante d'euleur

print(math.inf)

#Ce type speciale ce comporte comme l'infinie en mathematique

print(type(math.nan))

#On a nan qui est une valeur qu'on esperer etre un chiffre mais le type est float

print(math.gcd(18, 12, 24))

#Plus grand diviseur commun

print(math.lcm(18, 13, 7))

#Plus petit multiplicateur commun

print(math.fabs(-123))

#valeur absolu

print(math.fsum([23, 54 ,12, 12 ,90]))

#somme de l'iterable

print(math.factorial(5))

#Factoriel

print(math.comb(5,3))

#combinaison

print(math.perm(5,3))

#Permutation

print(math.trunc(8.12))

#Renvois la partie entiere

print(math.ceil(8.12))

#plafonne le chiffre reelle au prochaine entier

print(math.floor(8.12))

#renvois au chiffre le plus petit

#Plusieur autre fonctions arithmetique existe et viendront a l'avenir

print(math.sin(math.pi))

#Sinus de pi

print(math.cos(math.pi))

#Cosinus de pi

print(math.tan(math.pi))

#Tangente de pi

print(math.asin(math.sin(math.pi)))

#ArcSinus de pi

print (math.acos(math.cos(math.pi)))

#ArcCosinus de pi

print(math.atan(math.tan(math.pi)))

#ArcTangente de pi

print(math.sinh(2))

#Sinus hyperbolique de 2

print(math.cosh(2))

#Cosinus hyperbolique de 2

print(math.tanh(2))

#Tangente hyperbolique de 2

print(math.sinh(math.sinh(2)))

#ArcSinus hyperbolique de 2

print(math.acosh(math.cosh(2)))

#ArCosinus hyperbolique de 2

print(math.atanh(math.tanh(2)))

#ArTangente hyperbolique de 2

print(math.pow(2,3))

print(pow(2,3))

print(2**3)

#Les formes de puissance

print(math.exp(math.e))

#e^e

print(math.log(8,2))

#Log de 8 a la base 2

#Si on ne met pas le deuxieme parametre ca donne ln

print(math.sqrt(16))

#racine carre uniquement les entier et reel pas pour les complex
#Il ya encore beaucoups plus
