"""
Write a program to generate the following pattern in Python. From a given number n
*
**
***
****
"""

a = '*'

n = int(input("Entrer le nombre d'etages >"))

if n<=0:
    print("Le nombre est mauvais")
else :
    for i in range(1,n+1):
        print((i)*a,end='\n')
