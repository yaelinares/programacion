numeros=[1, 543, -76, 21, -8]
palabras=["Hola", "mar", "tierra", "fuego", "aire", "adios"]

# ¿Qué palabras contienen la letra 'r'?
for i in palabras:
   if "r" in i:
       print(i)
print("----------------------------")
# ¿Qué palabras contienen más de 4 caracteres?
for i in palabras:
    if len(i) > 4:
        print(i)
print("----------------------------")
# ¿Qué números son múltiplos de 3?
for i in numeros:
    if i%3 == 0:
        print(i)
print("----------------------------")
# ¿qué números son primos?
esPrimo = True
for i in numeros:
    if i > 0:
        esPrimo = True
        for j in range(2,i):
            if i % j == 0:
                esPrimo = False
        if esPrimo:
            print(i)