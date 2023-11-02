#Número par
numero = int(input("Dime un número: "))
if numero==0:
    print("Tu número no es valido")
elif numero %2==0:
    print("Tu número es par")
else:
    print("Tu número es impar")