#Dado un número vamos a decir en que franja de porcentaje se encuentra
numero = float(input("Dime un número: "))
if numero >=75 and numero <=100:
    print("tu número está entre 75 y 100")
elif numero >=50 and numero <75:
    print("tu número está entre 50 y 75")
elif numero >=25 and numero <50:
    print("tu número está entre 25 y 50")
elif numero >=0 and numero <25:
    print("tu número está entre 0 y 25")
else: 
    print("No está dentro del rango")