'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.'''

lista = []
x = int(input("Cuantas asignaturas tiene tu curso: \n"))
for i in range(x):
    if i == 0:
        a = input("Introduce la primera asignatura: ")
    else:
        a = input("Introduce la siguiente asignatura: ")
    lista.append(a)
print(lista)