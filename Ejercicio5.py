'''Escribir un programa que almacene en una lista los números del 1 al 10 y
 los muestre por pantalla en orden inverso separados por comas.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(lista), 0, -1):
    if i == 1:
        print(lista[i - 1])
    else:
        print(lista[i - 1], end=",")