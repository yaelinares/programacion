#Elementos que son pares e impares en una lista
lista=[1, 2, 4, 8, 16]
for numero in lista:
    if(numero%2==0):
        print(f"El {numero} es par")
    else:
        print(f"El {numero} es impar")
