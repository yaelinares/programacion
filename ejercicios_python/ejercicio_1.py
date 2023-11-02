#Ejercicio 1: Realizar un programa que almacene solamente 15 números pares en una lista.
lista=[]
contador = 0
while(contador<15):
    num = int(input("Dime un número par: "))
    if(num%2 == 0):
        lista.append(num)
        contador = contador + 1
    else:
        print("Es impar")
print(lista)