"""
Les operateurs speciaux

"""

a = 50

b = 49 + 1

c = a is b

print(c)

#L'operateur verifie si deux objet on un identifiantbqui point sur une meme valeur

# Ici omt aura false

c = a is not b

print(c)

#On aura true maintenant

a = (23, 78, 67)

b = 23

c = b in a

print(c)

#Verifie si une valeur est presente dans un sequence liste, tuple , dico

a = (23, 78, 67)

b = 23

c = b not in a

print(c)

#Verifie si une valeur n'est pas dans un tuple

a, b = b, a

print(a)

print(b)

#inverser les valeurs de a et de b

b = 12

print(a|b)

#Bitwise OR

print(a^b)

#Bitwise XOR

print(a&b)

#Bitwise AND

print(a>>2)

#Bitwise rigth shift

print(a<<2)

#Bitwise left shift

print(~a)

#Inverseur tranforme en negatif

#D'autre operateurs sont a decouvrir

#Les operateur bitwise s'utilise particulierement avec les int strictement positif



