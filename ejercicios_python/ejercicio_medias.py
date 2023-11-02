#nota media alumnos, por alumno y media general por asignatura
alumnos=[("Pepe",    [["Matemáticas", 5], ["Lengua", 9]]),
         ("Juan",    [["Matemáticas", 6], ["Lengua", 8]]),
         ("Matilde", [["Matemáticas", 8], ["Lengua", 8]]),
         ("Cloti",   [["Matemáticas", 3], ["Lengua", 5]]),
         ("Agus",    [["Matemáticas", 1], ["Lengua", 10]]),
        ]

def mediaMates():
    contador = 0
    resultado = 0
    for i in alumnos:
        #print(i[1][0][1], "---------",alumnos[contador][1][0][1]    ##Similares
        x = alumnos[contador][1][0][1]
        resultado += x
        contador += 1
    print("La media de matemáticas es:",resultado/len(alumnos))
#acumMates=0                                                        ##Con bucles anidados
#for i in alumnos:   
    #for j in i[1]:   
        #if(j[0]=="Matemáticas"):
            #print(j[1])
            #acumMates+=j[1]
    #print("-------", acumMates) 

mediaMates()

print("------------------------------------")

def mediaLengua():
    contador = 0
    resultado = 0
    for i in alumnos:
        x = alumnos[contador][1][1][1]
        resultado += x
        contador += 1
    print("La media de lengua es:",resultado/len(alumnos))

mediaLengua()
print("------------------------------------")

def mediaGeneral():
    contador = 0
    for i in alumnos:
        x = alumnos[contador][1][0][1]
        y = alumnos[contador][1][1][1]
        print(f"La media de {alumnos[contador][0]} es", (x + y)/2)
        contador += 1

mediaGeneral()