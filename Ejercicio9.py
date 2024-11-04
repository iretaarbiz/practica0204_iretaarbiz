palabra = list(input("Introduce una palabra para comprobar cuantas veces tiene cada vocal: \n"))
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0
for i in range(len(palabra)):
    if palabra[i] == "a" or palabra[i] == "A":
        contA += 1
    elif palabra[i] == "e" or palabra[i] == "E":
        contE += 1
    elif palabra[i] == "i" or palabra[i] == "I":
        contI += 1
    elif palabra[i] == "o" or palabra[i] == "O":
        contO += 1
    elif palabra[i] == "u" or palabra[i] == "U":
        contU += 1
print("La a aparece", contA, "veces")
print("La e aparece", contE, "veces")
print("La i aparece", contI, "veces")
print("La o aparece", contO, "veces")
print("La u aparece", contU, "veces")