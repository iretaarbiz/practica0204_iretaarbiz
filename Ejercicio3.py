''' Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota>
 donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''

listaNombres = []
listaNotas = []
x = int(input("Cuantas asignaturas tiene tu curso: \n"))
for i in range(x):
    if i == 0:
        a = input("Introduce la primera asignatura: ")
    else:
        a = input("Introduce la siguiente asignatura: ")
    listaNombres.append(a)
for j in range(len(listaNombres)):
    print("Introduce la nota de la asignatura", listaNombres[j])
    b = input()
    listaNotas.append(b)
for k in range(len(listaNombres)):
    print("En la asignatura", listaNombres[k], "has sacado", listaNotas[k])