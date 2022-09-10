# Ejercicio 3: Crear una función recursiva para sumar los números de una lista.
import time as time
import random as random
rango = 997
rangoRandomicos = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000**123542
valores = []
inicio=time.time()
for i in range(rango):
    valores.append(random.randint(0,rangoRandomicos))

#print("La lista de números es: ", valores)

def sumar_lista(numeros):
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + sumar_lista(numeros[1:])

resultado = sumar_lista(valores)
final= time.time() - inicio 

print('La suma es igual a: ', resultado)
print("tiempo: " + str(final))