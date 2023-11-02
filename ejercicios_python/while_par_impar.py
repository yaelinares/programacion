#Realizar un programa que me pida números y me detecte si son números impares.
#Estará pidiendo hasta que introduzcamos un número par
n=int(input("Dime un número par:" ))
while n%2!=0:
    print(f"{n} es impar")
    n=int(input("Dime un número par:" ))
print(f"{n} es par")