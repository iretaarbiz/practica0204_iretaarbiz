muestra = input("Introduce los números separados por comas: \n")
lista = muestra.split(",")
media = 0
varianza = 0
for i in range(len(lista)):
    media += int(lista[i])
media /= len(lista)
for j in(lista):
    varianza += ((media - i)**2)
varianza /= len(lista) 
print(media)
print(varianza)