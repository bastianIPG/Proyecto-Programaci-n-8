import matplotlib.pyplot as plt

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
    DatosF = []
    for linea in archivo:
        campos = linea.split(",") 
        if campos[0] == Region:
            for contador in range(len(campos)-15,len(campos)-1):
                DatosF.append(int(float(campos[contador])))
    archivo.close()
    return DatosF

def DatoRegionNoAcumulado(DatosF):
        DatosNoAcumulado= []
        for i in range(1,len(DatosF)):
            operacion = DatosF[i] - DatosF[i-1]
            DatosNoAcumulado.append(int(operacion))
        return DatosNoAcumulado

flag = True
while flag:
    option = input("[1] Ingrese el nombre o numero de la region: \n")
    if option == "1" or option == "Tarapacá":
        print("Region de Tarapacá")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Tarapacá")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Tarapaca 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "2" or option == "Antofagasta":
        print("Region de Antofagasta")
        epapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if epapa == "1":
            print("Datos Acumulativos")

        elif epapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Antofagasta")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Antofagasta 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "3" or option == "Atacama":
        print("Region de Atacama")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Atacama")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Atacama 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")


    if option == "4" or option == "Coquimbo":
        print("Region de Coquimbo")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Coquimbo")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Coquimbo 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos No acumulativos")

    if option == "5" or option == "Valparaíso":
        print("Region de Valparaíso")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Valparaíso")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Valparaiso 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")
    
    if option == "6" or option == "Bernardo Ohiggins":
        print("Region General Bernardo Ohiggins")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Bernardo Ohiggins")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Bernardo Ohiggins 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "7" or option == "Maule":
        print("Region del Maule")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Maule")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Maule 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "8" or option == "Biobío":
        print("Region del Biobío")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Biobío")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Biobío 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "9" or option == "Araucanía":
        print("Region de la Araucanía")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Araucanía")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Araucanía 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "10" or option == "Los Lagos":
        print("Region de Los Lagos")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Los Lagos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Los Lagos 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "11" or option == "Aysén":
        print("Region de Aysén")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Aysén")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Aysén 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "12" or option == "Magallanes":
        print("Region de Magallanes")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Magallanes")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Magallanes 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "13" or option == "Region Metropolitana":
        print("Region Metropolitana")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Region Metropolitana")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Region Metropolitana 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "14" or option == "Los Ríos":
        print("Region de Los Ríos")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Los Ríos")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Los Ríos 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "15" or option == "Arica y parinacota":
        print("Region de Arica y parinacota")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("Arica y parinacota")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid Arica y parinacota 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")

    if option == "16" or option == "Ñuble":
        print("Region del Ñuble")
        opapa = input("[1] Datos acumulativos \n" "[2] Datos no Acum \n" "ingrese: ") 
        if opapa == "1":
            print("Datos Acumulativos")
        elif opapa == "2":

            dias = ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"10" ,"11" ,"12", "13", "14"]
            casos = DatosRegion("niublrawdawd")
            colors = ["brown", "green", "red", "blue", "purple", "yellow", "pink", "grey", "brown", "green", "red", "blue", "purple", "yellow"]

            plt.title("Casos Covid asdawdawd 2019")
            plt.bar(dias, height=casos, color=colors)
            plt.show()

            print("Datos no acumulativos")
            
    elif option == "0":
        flag = False
print("Saliendo del programa....")
