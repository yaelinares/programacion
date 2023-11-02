#Calcular el área del cuadrado(el área de los 20 primeros cuadrados de lado par)
print("ÁREA CUADRADO")
cuenta = 0
for i in range(1, 41):
    if i%2 == 0:
        cuenta = cuenta + 1
        print(f"{cuenta}El area del cuadrado de lado {i} es {i*2}")