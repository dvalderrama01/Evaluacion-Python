"""3. Dada la siguiente lista:
numeros = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
a) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos. valor 0.3
b) Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos. valor 0.3"""

numeros = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

print("\nCiclo For\n")

for i in range (len(numeros)):
    print(numeros[i],end=' | ')

print("\nCiclo While\n")

i=0
while i in range(len(numeros)):
    print(numeros[i],end=' | ')
    i=i+1