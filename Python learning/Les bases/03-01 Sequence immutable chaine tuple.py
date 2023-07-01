"""

Les sequence immutable

"""

#Les string ou str

a = 'Bonjour'

print(type(a))

a = "Bonjour"

print(type(a))

a = """Bon
jour"""

print(type(a))

print(a)

#Les trois facon de representer les chaines de caracteres

#Transformer une variable en chaine on utilise str(une_variable)

a = 'abcdef'

print(a[0])

#On a 'a'

print(a[5:])

#On a 'f'

print(a[:5])

#On a tout les caractere avant le sixieme caractere 'abcde'

print(a[0:5])

#On a 'abcde' tout les caractere sauf le sixieme 

print(a[0:5:3])

#On a 'ad' ici on part du premier au sixieme en sautant de 3 - 1 pour dire 0 debut 5 fin 3-1 est le pas

print(a[-1])

#On a f recuperation apartir de derriere

#Plusieur autre option disponible avec les slice

#Impossible de faire

# a[2]='c'

#Voir la Doc pour les fonctions lies au chaine de caracteres split, len, upper, lower etc
