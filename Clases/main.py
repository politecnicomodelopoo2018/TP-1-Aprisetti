import json
import datetime
from Aviones import Avion
from Vuelo import Vuelo
from Sistema import Sistema
from Personas import Persona

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

    personaAux = eval(archivoDiccionario["tipo"])()
    personaAux.deserealizar(item)
    if personaAux.__class__.__name__  == "Piloto":
        listaPilotos.append(personaAux)
    elif personaAux.__class__.__name__ == "Servicio":
        listaServicios.append(personaAux)
    elif personaAux.__class__.__name__ == "Pasajero":
        listaPasajeros.append(personaAux)

for item in archivoDiccionario["Vuelos"]:

    vueloAux = Vuelo()
    vueloAux.deserializar(item)
    listaVuelos.append(vueloAux)

sistema.listaDeAviones = listaAviones
sistema.listaDePasajeros = listaPasajeros
sistema.listaDeVuelos = listaVuelos
sistema.listaDeTripulacion = listaPilotos + listaServicios