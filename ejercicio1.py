"""1. Cree una función que reciba como argumentos dos números y retorne el mayor de estos 
números, luego haga el llamado a la función y guarde su valor de retorno en una variable
e imprima ese valor por consola."""


def mayor_numeros(a,b):
    if n1<n2:
        numMayor=n2
    else:
        numMayor=n1

    return numMayor

n1=int(input("Ingrese el primer número "))
n2=int(input("Ingrese el segundo número"))

if n1>n2 or n2>n1:
    mayor=mayor_numeros(n1,n2)
    print("los números son:\n número 1: {0}\n número 2: {1}\nEl mayor es: {2}".format(n1,n2,mayor))
else:
    print("Los números son iguales, número 1: ({0}), número 2: ({1})".format(n1,n2))