import matplotlib.pyplot as plt #Import para las graficas
def LsitReg(): #Definición en la cual se buscaran los nombres de la region, para luego filtrarlas al usuario
    with open("CasosNuevosSinSintomas.csv","r", encoding="utf-8") as f:
        Regiones = [] 
        for i in f.readlines(): #Comenzara a leer cada linea encontrando las regiones.
            lista = i.split(",")
            if lista[0] not in Regiones and lista[0]!= "Region" and lista[0] != "Total": #Si la lista se encuentra "region" y "total" estas serian ignoradas para asi solo printear las Regiones
                Regiones.append(lista[0])
        print(Regiones)
LsitReg()

def DatosRegion(Region): #Datos region funcionara como el que comienza la busca de los datos no acumulados.
    archivo = open("CasosNuevosSinSintomas.csv","r", encoding="utf-8")
    FiDatos = [] #Lista vacia en la cual se almacenan los datos.
    for linea in archivo: #Comenzara desde el inicio de las regiones en las cuales se filtraran los datos.
        campos = linea.split(",") 
        if campos[0] == Region:
            for contador in range(len(campos)-15,len(campos)-1): #Aqui solo tomaremos los datos de las ultimas 2 semanas.
                FiDatos.append(int(float(campos[contador])))
    archivo.close()
    return FiDatos

def DatoRegionAcumulado(Region): #Definicion para los datos acumulados.
    archivo = open("CasosNuevosSinSintomas.csv","r", encoding="utf-8")
    DatosAcumulado= []
    for linea in archivo: #Se tomaran las lineas en el archivo
        campos = linea.split(",") 
        if campos[0] == Region:
            Akum=0 #Akum es el contador de los acumulados, el nombre puesto por falta de ideas.
            for i in range(len(campos)-15,len(campos)-1): #Tal como el anterior se buscaran los datos de la ultimas 2 semanas
                Akum += int(float(campos[i])) #Se convierten los datos para campos y luego asi se añaden a Akuma para sumarlos, luego de eso se dan los Casos acumulados.
                DatosAcumulado.append(Akum)
    archivo.close()
    return DatosAcumulado
             
flag = True
while flag: #While para el inicio del menu, asi para que el usuario pueda buscar tranquilamente base algunas cuantas mecanicas.
    option = input("[1] Ingrese el nombre o numero de la region: \n")
    if option == "1" or option == "Tarapacá": #Se pueden poner numeros, como el da las regiones en este caso por si alguien no conoce el nombre
        print("Region de Tarapacá")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acumulativos \n" "ingrese: ") 
        if op == "1": #Aqui comienza a mostrar el grafico.
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Tarapacá") #Para que funcione se llama a la funcion junto a la region cual nosotros ingresamos.
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulativos Tarapaca 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2": #Mostrar grafico no acumulados.
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Tarapacá")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulativos Tarapaca 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "2" or option == "Antofagasta":
        print("Region de Antofagasta")
        epapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if epapa == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Antofagasta")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Antofagasta 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif epapa == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Antofagasta")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Antofagasta 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "3" or option == "Atacama":
        print("Region de Atacama")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Atacama")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Atacama 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Atacama")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Atacama 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "4" or option == "Coquimbo":
        print("Region de Coquimbo")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Coquimbo")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Coquimbo 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Coquimbo")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Coquimbo 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos No acumulativos")

    if option == "5" or option == "Valparaíso":
        print("Region de Valparaíso")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Valparaíso")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Valparaiso 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Valparaíso")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Valparaiso 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")
    
    if option == "6" or option == "O’Higgins":
        print("Region General Bernardo Ohiggins")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("O’Higgins")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Bernardo Ohiggins 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("O’Higgins")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Bernardo Ohiggins 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "7" or option == "Maule":
        print("Region del Maule")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Maule")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Maule 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Maule")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Maule 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "8" or option == "Biobío":
        print("Region del Biobío")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Biobío")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Biobío 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Biobío")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Biobío No Acumulado 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "9" or option == "Araucanía":
        print("Region de la Araucanía")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Araucanía")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Araucanía 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Araucanía")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Araucanía 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "10" or option == "Los Lagos":
        print("Region de Los Lagos")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Los Lagos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Los Lagos 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Los Lagos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Los Lagos 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "11" or option == "Aysén":
        print("Region de Aysén")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Aysén")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Aysén 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Aysén")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Aysén 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "12" or option == "Magallanes":
        print("Region de Magallanes")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Magallanes")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Magallanes 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Magallanes")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Magallanes 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "13" or option == "Metropolitana":
        print("Region Metropolitana")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Metropolitana")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Region Metropolitana 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Metropolitana")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado RM 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "14" or option == "Los Ríos":
        print("Region de Los Ríos")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Los Ríos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Los Ríos 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Los Ríos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Los Ríos 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "15" or option == "Arica y Parinacota":
        print("Region de Arica y parinacota")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Arica y Parinacota")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulado Arica y parinacota 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Arica y Parinacota")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulado Arica y parinacota 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")

    if option == "16" or option == "Ñuble":
        print("Region del Ñuble")
        op = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if op == "1":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatoRegionAcumulado("Ñuble")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid Acumulativos Ñuble 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos Acumulativos")
        elif op == "2":
            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Ñuble")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]
            plt.title("Casos Covid No Acumulativos Ñuble 2021")
            plt.bar(dias, height=casos, color=colors)
            plt.show()
            print("Datos no acumulativos")
    elif option == "0": #Ya como la persona presione 0 saldra del programa haciendo que el while sea falso.
        flag = False
print("Saliendo del programa....")
