import json
import datetime
from Aviones import Avion
from Personas import *
from Vuelo import Vuelo
from Sistema import Sistema
from Funciones import *
from flask import Flask, render_template

app = Flask(__name__)




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

    if personaAux.__class__.__name__ == "Servicio" or personaAux.__class__.__name__ == "Piloto":
        personaAux.deserealizar(item, listaAviones)
    elif personaAux.__class__.__name__ == "Pasajero":
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

pagesite = 0

for item in listaVuelos:
    pagesite += 1
    '''
    print("\n"*3 + "El avion de este vuelo es el: " + item.avion.codigoUnico + "\n")
    print("Tripulacion del vuelo: " + item.avion.codigoUnico + "\n")
    print(sistema.mostrarPasajeroEnVuelo(item))
    print("El pasajero mas joven es: ")
    print("     " + sistema.mostrarPasajeroMasJovenEnVuelo(item).nombre + " "
          + sistema.mostrarPasajeroMasJovenEnVuelo(item).apellido)
    print("\n")

    tripulacion = sistema.mostrarminimaTripulacion(item)

    if tripulacion != None:
        print("Vuelo " + tripulacion.avion.codigoUnico +  " cumple cantidad de tripulacion")

    tripulacionNoAutorizada = sistema.mostrarTripulacionNoAutorizada(item)

    if tripulacionNoAutorizada != None:
        print("Vuelo " + tripulacionNoAutorizada.avion.codigoUnico + " no cumple con tripulacion autorizada")
    print("\n")

    print("Personas vip o con necesidades especiales en el vuelo: ")

    cosasVip = sistema.mostrarPersonaEspecial(item)
    if cosasVip != None:
        for cosa in cosasVip:
            print("     Nombre: " + cosa.nombre + " " + cosa.apellido)
            print("     DNI: " + cosa.dni)
        print("\n")

    idiomas = sistema.mostrarListaIdiomas(item)
    for idiom in idiomas:
        print("Idioma del vuelo: " + idiom + "\n")



print("\n" + "Tripulacion que vuela mas de una vez: ")
for item in sistema.tripulacionQueVuelaMasDeUnaVez():
    print("     Nombre: " + item.nombre + " " + item.apellido + "\n")
'''
for item in sistema.listaDeVuelos:
    print(inicio(item))
    print(ejercicio1(item))
    print(ejercicio2(item))
    print(ejercicio3(item))
    print(ejercicio4(item))
    print(ejercicio5(item))
    print(ejercicio6(item))
    print(ejercicio7(item))

@app.route("/")
def vuelos():
    return render_template("index.html", listaDeVuelos = sistema.listaDeVuelos)

@app.route("/<vuelo>")
def vuelo(vuelo):
        return render_template("Vuelos.html", name=vuelo,
                               listaDeVuelos = sistema.listaDeVuelos,
                               sistema = sistema)

if __name__ == "__main__":
    app.run(debug=True)