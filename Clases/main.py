import json
import datetime
from Aviones import Avion
from Personas import *
from Vuelo import Vuelo
from Sistema import Sistema

sistema = Sistema()
listaAviones = []
listaPilotos = []
listaServicios = []
listaPasajeros = []
listaVuelos = []

with open("datos.json", "r") as f:
    archivoDiccionario = json.loads(f.read())

for item in archivoDiccionario["Aviones"]:
    avionAux = Avion()
    avionAux.deserealizar(item)
    listaAviones.append(avionAux)

for item in archivoDiccionario["Personas"]:
    personaAux = eval(item["tipo"])()
    if eval(item["tipo"])() == ("Servicio" or "Piloto"):
        personaAux.deserealizar(item, listaAviones)
    else:
        personaAux.deserealizar(item)
    if personaAux.__class__.__name__  == "Piloto":
        listaPilotos.append(personaAux)
    elif personaAux.__class__.__name__ == "Servicio":
        listaServicios.append(personaAux)
    elif personaAux.__class__.__name__ == "Pasajero":
        listaPasajeros.append(personaAux)

for item in archivoDiccionario["Vuelos"]:
    vueloAux = Vuelo()
    vueloAux.deserializar(item, listaPasajeros, listaPilotos, listaServicios, listaAviones)
    listaVuelos.append(vueloAux)

sistema.listaDeAviones = listaAviones
sistema.listaDePasajeros = listaPasajeros
sistema.listaDeVuelos = listaVuelos
sistema.listaDeTripulacion = listaPilotos + listaServicios

for item in listaVuelos:

    print(sistema.mostrarPasajeroEnVuelo(item))
    print("El pasajero mas joven es: ")
    print(sistema.mostrarPasajeroMasJovenEnVuelo(item).nombre + " "
          + sistema.mostrarPasajeroMasJovenEnVuelo(item).apellido)
    print("\n")

    tripulacion = sistema.mostrarminimaTripulacion(item)
    print("Vuelo no cumple cantidad de tripulacion: ")
    if tripulacion != None:
        print(tripulacion.avion.codigoUnico)
    print("\n")

    tripulacionNoAutorizada = sistema.mostrarTripulacionNoAutorizada(item)
    print("Vuelo no cumple con tripulacion autorizada: ")
    if tripulacionNoAutorizada != None:
        print(tripulacionNoAutorizada.avion.codigoUnico)
    print("\n")

    print("Personas vip o con necesidades especiales en el vuelo: ")

    cosasVip = sistema.mostrarPersonaEspecial(item)
    if cosasVip != None:
        for cosa in cosasVip:
            print("Nombre: " + cosa.nombre + " Apellido: " + cosa.apellido + "\n")
        print("\n")

    idiomas = sistema.mostrarListaIdiomas(item)
    for idiom in idiomas:
        print("Idioma del vuelo: " + idiom + "\n")


print("\n" + "Tripulacion que vuela mas de una vez: ")
for item in sistema.tripulacionQueVuelaMasDeUnaVez():
    print("Nombre: " + item.nombre + " Apellido: " + item.apellido + "\n")