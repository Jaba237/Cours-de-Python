"""
La boucle for et les iterateur

"""

outil=['planche','clou','niveleur','angle','metre','scie','marteau']

#Utilisons le for pour navigeuz dans cette structure

for i in outil:
    print(i)

#Transformon notre liste en iterateurs et parcourront la

outil_iter = iter(outil)

print(type(outil_iter))

#Une iterateur de type liste
#C'est ainsi que la boucle for ce comporte

print(next(outil_iter))
print(next(outil_iter))
print(next(outil_iter))
print(next(outil_iter))
print(next(outil_iter))
print(next(outil_iter))
print(next(outil_iter))
#print(next(outil_iter)) la ligne de trop

#La fonction next() navigue dans la liste apartir du premier element au premier appel
#et dans les appel qui suivent elle nous ramene le suivant

for i in range(len(outil)):
    print(outil[i])

#Dans le cas present nous utilisons la boucle pour grace a un compteur genere par
#la fonction range() elle peut prendre 3 parametre
#Quand on met un parametre dit n alors on va cree une liste d'entier qui va aller de 0 a n-1 apartir de laquelle le compteur tire sa valeur
#Quand on met deux parametre n et m on va cree une liste d'entier qui va de n a m-1
#Si on ajout un troisieme parametre il s'agit du pas

for i in range(0,11,2):
    print(i)
#La liste de nombres pair de 0 a 10 
#Si on a des dictionaire utiliser le for nous donnera seulement les cles
dico = {'Aamal':1, 'Bamal':2, 'Camal':3, 'Damal':4, 'Eamal':5}

for x in dico:
    print(x)

#Si on veut les valeurs
for x in dico.values():
    print(x)
#La fonction values

