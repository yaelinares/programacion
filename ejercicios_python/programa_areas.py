#Realizar un programa que calcule el área de n figuras geométricas.
#Preguntará primeramente de qué figura queremos realizar el área
#Seguidamente y tras comprobar que esa figura es válida, pedirá los 
#datos necesarios por teclado para poder realizar los cálculos
#Una vez hayamos realizado el área, almacenaremos en una estructura los datos
#de esa figura (nombre, parámetrosArea, área)  y preguntaremos si queremos 
#seguir calculando áreas de figuras geométricas.
#En caso de no querer, terminaremos si seleccionamos la opción "NO"
#[
# ("Triángulo", (3,2), 3),
# ("Cuadrado", (4), 16),
# ("Cuadrado", (7), 49),
# ("Triángulo", (2, 4), 4)
#]

import math

def cuadradoArea(l):
    return l*l
def rectanguloArea(b,h):
    return b*h
def trianguloArea(b, h):
    return(b*h)/2
def circuloArea(radio):
    return radio**2*math.pi
lista=[]
while True:
    x = input("Qué figura quieres que sea:\nCuadrado,\nRectangulo,\nCirculo,\nTriangulo\n('NO' para finalizar el programa): ")
    palabra = x.upper()
    if palabra == "CUADRADO":
        l = float(input("Cual es el lado del Cuadrado: "))
        lista += [(palabra,(l), cuadradoArea(l))]
        
    elif palabra =="RECTANGULO":
        b = float(input("Cual es la base del Rectángulo: "))
        h = float(input("Cual es la altura del Rectángulo: "))
        lista += [(palabra,(b, h), rectanguloArea(b, h))]
        
    elif palabra =="CIRCULO":
        radio = float(input("Cual es el radio del Círculo: "))
        lista += [(palabra,(radio), circuloArea(radio))]
        
    elif palabra =="TRIANGULO":
        b = float(input("Cual es la base del Triángulo: "))
        h = float(input("Cual es la altura del Triángulo: "))
        lista += [(palabra,(b, h), trianguloArea(b, h))]
        
    elif palabra == "NO":
        print(lista)
        print("Programa terminado")
        break