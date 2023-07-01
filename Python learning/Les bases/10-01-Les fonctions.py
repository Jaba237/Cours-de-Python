"""
Les fonction en Python

"""

def addition_parametre_retour(a,b):
    return a+b

def addition_sans_parametre_retour():
    a=int(input("Entrer un nombre"))
    b=int(input("Entrer un autre nombre"))
    return a+b

def addition_sans_parametre_sans_retour():
    a=int(input("Entrer un nombre"))
    b=int(input("Entrer un autre nombre"))
    print(a+b)
    
une_variable_de_fonction_lambda = lambda a,b:a+b


z = int(input("Entrer un nombre"))
y = int(input("Entrer un autre nombre"))

print(addition_parametre_retour(z,y))

print(addition_sans_parametre_retour())

addition_sans_parametre_sans_retour()

print(une_variable_de_fonction_lambda(z,y))

#Appel de la fonction
