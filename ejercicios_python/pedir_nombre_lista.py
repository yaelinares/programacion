# Realizar un programa que me pida el nombre de un usuario y lo siga pidiendo si el usuario no se encuentra en una lista de nombres creada inicialmente (5 nombres)
n=input("Dime tu nombre: ")
l=["andres", "javier", "alberto", "ivan", "yael"]
while n not in l:
    print(f"{n} no esta en la lista")
    n=input("Dime tu nombre: ")
print(f"{n} esta en la lista ")