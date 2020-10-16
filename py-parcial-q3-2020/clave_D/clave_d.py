import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar():
    n1 = 2
    n2 = 4
    n3 = 3
    result = n1*n2*n3
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    n = 1000
    suma = 0
    while 1000<=n<=2000:
        if (n%3==0) and (n%5==0):
            suma += n
            n += 1
        else:
            n += 1
    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro():
    ortoDict = {"area": obtenerArea(), "volumen": obtenerVolumen()}
    result = ortoDict
    return result


def obtenerArea():
    longitud = 10
    latitud = 6
    altura = 5
    a1 = (longitud*latitud+longitud*altura+latitud*altura)
    a2 = 2*a1
    result = a2
    return result


def obtenerVolumen():
    longitudv = 10
    latitudv = 6
    alturav = 5
    result = longitudv*latitudv*alturav
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def definicionOrtoedro(self):
        ortoDict = {"area": obtenerArea(), "volumen": obtenerVolumen()}
        result = ortoDict
        return result


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        listaComputadora = []
        computadora[0] = dict(procesador="intel", ram="16gb", tarjeta="nvidia", ssd="240gb", costo=700.0, conDescuento="false", descuento=0.0, conPlazo="false", cuota=0.0)
        computadora[1] = dict(procesador="amd", ram="16gb", tarjeta="nvidia", ssd="512gb", costo=750.0, conDescuento="True", descuento=20.0, conPlazo="false", cuota=0.0)
        computadora[2] = dict(procesador="intel", ram="8gb", tarjeta="nvidia", ssd="240gb", costo=700.0, conDescuento="false", descuento=0.0, conPlazo="false", cuota=0.0)
        computadora[3] = dict(procesador="amd", ram="16gb", tarjeta="nvidia", ssd="512gb", costo=700.0, conDescuento="True", descuento=50.0, conPlazo="false", cuota=0.0)
        computadora[4] = dict(procesador="intel", ram="16gb", tarjeta="nvidia", ssd="1Tb", costo=700.0, conDescuento="True", descuento=70.0, conPlazo="false", cuota=0.0)
        computadora[5] = dict(procesador="intel", ram="32gb", tarjeta="nvidia", ssd="2Tb", costo=900.0, conDescuento="false", descuento=0.0, conPlazo="false", cuota=0.0)

        i=0
        while i<=5:
            listaComputadora.append(computadora[i])

        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/TeresaEngelhard/parcial1"
