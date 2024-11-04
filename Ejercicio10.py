precios = [50, 75, 46, 22, 80, 65, 8]
mayor = 0
menor = precios.max()
for i in range(precios):
    if mayor <= i:
        mayor = i
    elif menor >= i:
        menor = i