from Sistema import *

sistema = Sistema()

def inicio(vuelo):
    respusta = ("Este es el vuelo: %s - %s " % (vuelo.origen, vuelo.destino))

    return respusta

def ejercicio1(vuelo):
    respuesta = "Tripulacion del vuelo:  %s - %s \n" % (vuelo.origen, vuelo.destino) \
                + sistema.mostrarPasajeroEnVuelo(vuelo)

    return respuesta

def ejercicio2(vuelo):
    respuesta = ("El pasajero mas joven es: " + sistema.mostrarPasajeroMasJovenEnVuelo(vuelo).nombre + " "
                + sistema.mostrarPasajeroMasJovenEnVuelo(vuelo).apellido)
    return respuesta

def ejercicio3(vuelo):
    tripulacion = sistema.mostrarminimaTripulacion(vuelo)

    if tripulacion != None:
        respuesta = ("Vuelo %s - %s cumple con la cantidad de tripulacion necesaria" % (vuelo.origen, vuelo.destino))
    else:
        respuesta = ("Vuelo %s - %s NO cumple con la cantidad de tripulacion necesaria" % (vuelo.origen, vuelo.destino))
    return respuesta

def ejercicio4(vuelo):
    tripulacionNoAutorizada = sistema.mostrarTripulacionNoAutorizada(vuelo)
    if tripulacionNoAutorizada != None:
        respuesta = ("Vuelo %s - %s NO cumple con tripulacion autorizada" % (vuelo.origen, vuelo.destino))
    else:
        respuesta = ("Vuelo %s - %s cumple con tripulacion autorizada" % (vuelo.origen, vuelo.destino))

    return respuesta

def ejercicio6(vuelo):
    respuesta = "Personas vip o con necesidades especiales en el vuelo %s - %s: " % (vuelo.origen, vuelo.destino) + "\n"
    cosasVip = sistema.mostrarPersonaEspecial(vuelo)
    if cosasVip != None:
        for item in cosasVip:
            respuesta += "     Nombre: %s %s " % (item.nombre, item.apellido) + "\n" + "     DNI: %s" % item.dni + "\n"
    else:
        respuesta += "No hay personas VIP o con necesidades especiales en este vuelo" \

    return respuesta

def ejercicio7(vuelo):
    idiomas = sistema.mostrarListaIdiomas(vuelo)
    respuesta = "Idiomas del vuelo: " + "\n"
    for idioma in idiomas:
        respuesta += idioma + "\n"

    return respuesta

def ejercicio5(vuelo):
    respuesta = "Tripulacion que vuela mas de una vez: \n"
    procedimiento = sistema.tripulacionQueVuelaMasDeUnaVez(vuelo)
    for item in sistema.tripulacionQueVuelaMasDeUnaVez(vuelo):
        respuesta += "     Nombre: %s %s \n"  % (item.nombre, item.apellido)
    if len(procedimiento) == 0:
        respuesta = ""
    return respuesta
