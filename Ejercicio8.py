palabra = list(input("Introduce una palabra para comprobar si es un palíndromo: \n"))
palabravuelta = list(palabra)
palabravuelta.reverse()
if palabra == palabravuelta:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")