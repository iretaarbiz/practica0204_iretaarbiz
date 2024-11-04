abcd = list("abcdefghijklmnñopqrstuvwxyz")
borrar = []
for i in range(3, len(abcd), 3):
    borrar.append(abcd[i])
for j in(borrar):
    abcd.remove(j)
print(abcd)