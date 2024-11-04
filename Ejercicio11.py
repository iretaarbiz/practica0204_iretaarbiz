a = [[1, 2, 3], 
     [4, 5, 6]]
b = [[-1, 0], 
     [0, 1], 
     [1, 1]]
sumas = []
res = []
lista = []
for i in range(len(a)):
    for k in range(len(a)):
        suma = 0
        for j in range(len(a[i])):
            operacion = a[k][j] * b[j][i]
            suma = suma + operacion
            sumas.append(suma)
for m in range(2, len(sumas), 3):
    res.append(sumas[m])
print(res)
for n in range(0, len(res), 2):
    lista.insert(n, [res[n], res[n+1]])
print(lista)