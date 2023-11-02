#Números primos
num = int(input("Dime un número: "))
esPrimo = True
for i in range(2,num):
    if num % i == 0:
        esPrimo = False
        break  
if esPrimo:
    print("Es primo")
else:
    print("No es primo")