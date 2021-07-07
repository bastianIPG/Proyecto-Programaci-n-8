def LsitReg():
    with open("CasosNuevosSinSintomas.csv","r", encoding="utf-8") as f:
        Regiones = []
        for i in f.readlines():
            lista = i.split(",")
            if lista[0] not in Regiones and lista[0]!= "Region" and lista[0] != "Total":
                Regiones.append(lista[0])
        print(Regiones)
LsitReg()

def DatosRegion(Region):
    archivo = open("CasosNuevosSinSintomas.csv","r", encoding="utf-8")
    for linea in archivo:
        campos = linea.strip().split(",")
        región = campos[0]

flag = True
while flag:
    option = input("[1] Ingrese el nombre o numero de la region: \n")
    if option == "1" or option == "Tarapaca":
        print("Region de Tarapaca")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")
            print
    if option == "2" or option == "Antofagasta":
        print("Region de Antofagasta")
        epapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if epapa == "1":
            print("Datos Acumulativos")

        elif epapa == "2":
            print("datos acumi")

    if option == "3" or option == "Atacama":
        print("Region de Atacama")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "4" or option == "Coquimbo":
        print("Region de Coquimbo")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "5" or option == "Valparaiso":
        print("Region de Valparaiso")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")
    
    if option == "6" or option == "Bernardo Ohiggins":
        print("Region General Bernardo Ohiggins")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "7" or option == "Maule":
        print("Region del Maule")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "8" or option == "Biobío":
        print("Region del Biobío")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")
    if option == "9" or option == "Araucania":
        print("Region de la Araucania")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "10" or option == "Los lagos":
        print("Region de Los lagos")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "11" or option == "Aysen":
        print("Region de Aysen")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "12" or option == "Magallanes":
        print("Region de Magallanes")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "13" or option == "Region Metropolitana":
        print("Region Metropolitana")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "14" or option == "Los rios":
        print("Region de Los rios")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "15" or option == "Arica y parinacota":
        print("Region de Arica y parinacota")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")

    if option == "16" or option == "Ñuble":
        print("Region del Ñuble")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":
            print("datos acum")
    elif option == "0":
        flag = False
print("Saliendo del programa....")