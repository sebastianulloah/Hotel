#hotel
from json import load,dump
try:
    open("Archivo_json","x")
except:
    print("Archivo ya creado")
piezas = []
informacion =[]
for i in range (1,6):
    for j in range (1,6):
        piezas.append([f"{i}{j}","Disponible",])
def ver_piezas(lista):
    for i in lista:
        print (i, end="\t")
    print ()
def validacion_pieza():
    while True:
        try:
            num = int (input ("Ingrese el número de pieza:"))
            if num > 10 and num < 16:
                return num
            elif num > 20 and num < 26:
                return num
            elif num > 30 and num < 36:
                return num
            elif num > 40 and num < 46:
                return num
            elif num > 50 and num < 56:
                return num
            else:
                print ("Error: pieza no existe")
        except (ValueError):
            print ("Error: tipo de valor invalido")
        
    
def ingreso(lista, a):
    a = str(a)
    for i in lista:
        if a == i[0] and i[1] == "Disponible":
            while True:
                try:
                    b = int (input("Ingrese la cantidad de huespedes (Maximo 3)\n>"))
                    if b < 0:
                        print ("Error: el número de huespedes no puede ser menor a 0")
                    elif b > 4:
                        print ("Error: el número de huespedes no puede ser mayor a 3")
                    else:
                        for j in range (b):
                            i.append(input("Ingrese nombre:\n> "))
                            i.append(validacion_rut())
                            i[1] = "Ocupada"
                        print ("¡Ingreso exitoso!")
                        return True
                except (ValueError):
                    print ("Error: Tipo de dato invalido")
        elif a == i [0] and i [1] == "Ocupada":
            print ("Pieza ocupada")
            return False
def validacion_rut():
    while True:
        try:
            rut = int (input("Ingrese el rut (si el digito verificador es 'K' reemplacelo por un 0)\n>"))
            if rut < 10000000 or rut > 300000000:
                print ("Error: el rut no existe")
            else:
                print ("Rut encontrado:")
                return rut
        except (ValueError):
            print("Error: el rut no puede contener ni puntos ni guión")
def modificacion(lista, a):
    ciclo = True
    while ciclo:
        try:
            a = str(a)
            for i in lista:
                if a == i[0]:
                    estado = i[1]
                    print(f"Pieza encontrada. Estado: {estado}")
                    b = int(input ("Ingrese a que estado lo quiere cambiar:\n1.- Disponible\n2.-Reservada\n3.-Ocupada\n>"))
                    if b == 1:
                        i[1] = "Disponible"
                        del i[2:]
                        ciclo = False
                    elif b ==2:
                        i[1] = "Reservada"
                        ciclo = False
                    elif b == 3:
                        i[1] = "Ocupada"
                        ciclo = False
                    else:
                        print ("Error, opcion no indicada en el mení")
        except (ValueError):
            print("Error: tipo de valor invalido")
def eliminacion (lista, a):
    a = str(a)
    for i in lista:
        if a == i[0] and (i[1] == "Ocupada" or i[1] == "Reservada"):
            print ("Pieza encontrada")
            print("Ingrese el rut del primer huesped ingresado")
            if validacion_rut() == i[3]:
                print ("Eliminacion exitosa")
                del i[2:]
                i[1] = "Disponible"
                return True
        elif a == i[0] and i[1] == "Disponible":
            print ("Error: pieza no tiene asociada ninguna reserva")
            return False
def archivo(lista, archivo):
    for i in lista:
        diccionario ={}
        #print (f"hola soy la pieza {i[0]}")
        diccionario["Pieza"] = i[0]
        diccionario["Estado"] = i[1]
        if len(i) == 2:
            diccionario ["Huesped/s"] = i[2:]
        elif len(i) == 4:
            diccionario["Huesped 1"] = i [2]
            diccionario["Rut huesped 1"] = i[3]
        elif len(i) == 6:
            diccionario["Huesped 1"] = i [2]
            diccionario["Rut huesped 1"] = i[3]
            diccionario["Huesped 2"] = i [4]
            diccionario["Rut huesped 2"] = i[5]
        elif len(i) == 8:
            diccionario["Huesped 1"] = i [2]
            diccionario["Rut huesped 1"] = i[3]
            diccionario["Huesped 2"] = i [4]
            diccionario["Rut huesped 2"] = i[5]
            diccionario["Huesped 3"] = i [6]
            diccionario["Rut huesped 3"] = i[7]
        informacion.append(diccionario)
    with open(archivo,"w") as archivo_json:
        dump(informacion, archivo_json,indent = 1)
while True:
    try:
        opcion = (int(input("Menú de acciones: \n1.-Consultar piezas\n2.-Ingresar huesped\n3.-Modificar informacion pieza\n4.-Eliminar reserva\n5.-Generar archivo\n6.-Salir\n>")))
        match opcion:
            case 1:
                ver_piezas(piezas)
            case 2:
                print("Ingresando huesped")
                ingreso(piezas, validacion_pieza())
            case 3:
                print ("Modificando informacion")
                modificacion(piezas, validacion_pieza())
            case 4:
                print ("Eliminando reserva")
                eliminacion(piezas, validacion_pieza())
            case 5:
                print ("Generando archivo")
                archivo(piezas, "Archivo_json")
            case 6:
                print ("Saliendo")
                break
            case _:
                print("Error: opcion no disponible en el menú")
    except (ValueError):
        print ("Error: Tipo de valor invalido")
