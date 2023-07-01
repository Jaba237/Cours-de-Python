"""
Les sequences mutable

"""

a = []

#Liste vide

a = [[1,2,3], 3, False, 3.78, 10 + 12j, "Honda"]
print(a)

#Element heterogene dans la list

print(a[0:5:4])

#Slice d'une liste on aura [1,2,3] et 10+12j

a[0] = (1,2,3)
print(a)

#Modifie la valeur des elements d'une liste est possible

#Voir dans la doc les fonction lie au listes append, pop, push, retrive




