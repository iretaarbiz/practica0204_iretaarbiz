'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
 los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''

lista = []
x = int(input("Cuantos números ganadores ha habido? "))
for i in range(x):
    ganadores = input("Cuales son los números ganadores de la lotería primitiva: \n")
    lista.append(ganadores)
lista.sort()
print(lista)