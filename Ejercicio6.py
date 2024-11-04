'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.'''

listaNombres = []
listaNotas = []
borrar = []
cont = 0
x = int(input("Cuantas asignaturas tiene tu curso: \n"))
for i in range(x):
    if i == 0:
        a = input("Introduce la primera asignatura: ")
    else:
        a = input("Introduce la siguiente asignatura: ")
    listaNombres.append(a)
for j in range(len(listaNombres)):
    print("Introduce la nota de la asignatura", listaNombres[j])
    b = int(input())
    listaNotas.append(b)
for k in range(len(listaNotas)):
    if listaNotas[k] >= 5:
        borrar.append(listaNombres[k])
for l in(borrar):
        listaNombres.remove(l)
print(listaNombres)
    