#Ejercicio tupla con listas
n1 = input("Dime un nombre: ")
e1 = int(input("¿Cuántos años tiene?: "))
n2 = input("Dime un nombre: ")
e2 = int(input("¿Cuántos años tiene?: "))
n3 = input("Dime un nombre: ")
e3 = int(input("¿Cuántos años tiene?: "))
nombres = [n1, n2, n3]
edades = [e1, e2, e3]
#lista1 = [n1, e1] #Lo que está comentado sería otra forma
#lista2 = [n2, e2]
#lista3 = [n3, e3]
#tupla = (lista1, lista2, lista3)
tupla = ([nombres[0],edades[0]], [nombres[1],edades[1]], [nombres[2],edades[2]])
print(tupla)