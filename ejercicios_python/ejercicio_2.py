#Ejercicio 2: Realizar un programa que almacene palabras que empiecen solamente por la
#letra 'A' (mayúscula o minúscula) y termine cuando introduzcamos la palabra "Adios".
lista=[]
while True:
    palabra = input("Dime una palabra que empiece por la letra 'a': ")
    palabramayus = palabra.upper()
    if palabramayus == "ADIOS":
        print("Programa terminado")
        break
    elif palabramayus[0] == "A":
        lista.append(palabramayus)
    else:
        print("Tu palabra no empieza por A")