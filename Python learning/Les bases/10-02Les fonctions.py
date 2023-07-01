"""
Arguments d'une fonction

"""

def sum(*nombres):
    total = 0
    for x in nombres:
        total = total + x
    return total
#Plusier parametre

def table_multiplication(n, m=10):
    i = 1
    while i<=m:
        print(n," * ",i," = ",n*i)
        i+=1
#par defaut

def capital_pays(**keyword):
    if 'Yaounde' in keyword.values():
        print('Cameroun')
#Mot cles

print(sum(12,34,12,67,89,23))
table_multiplication(12,m=12)
capital_pays(AC='Yaounde',AO='Abuja',AN='Caire')

#Variables global

#my_val = 100

#def adi():
  #  global my_val
    #declaration d'une variable globale
 #   my_val = 200 + my_val
#print(my_val)
