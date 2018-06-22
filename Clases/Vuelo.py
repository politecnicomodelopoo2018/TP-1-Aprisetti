from datetime import *
from Personas import Persona

class Vuelo:

    def __init__(self, avion = None, fecha = None, hora = None, origen = None, destino = None):

        self.avion = avion
        self.fecha = fecha
        self.hora = hora
        self.origen = origen
        self.destino = destino

        self.tripulacion = []
        self.pasajeros = []

    def deserializar(self, archivoVuelo, listaPersonas, listaPilotos, listaServicios):

        self.avion = archivoVuelo["avion"]
        self.fecha = datetime.strptime(archivoVuelo["fecha"], "%Y-%m-%d").date()
        self.hora = archivoVuelo["hora"]
        self.origen = archivoVuelo["origen"]
        self.destino = archivoVuelo["destino"]

        for item in archivoVuelo["pasajeros"]:
            for persona in listaPersonas:
                if persona.dni == item:
                    self.pasajeros.append(persona)


        for item in archivoVuelo["tripulacion"]:
            for pilotos in listaPilotos:
                if pilotos.dni == item:
                    self.tripulacion.append(pilotos)
            for servicio in listaServicios:
                if servicio.dni == item:
                    self.tripulacion.append(servicio)


    def mostrarListaPasajeros(self):
        lista = ""
        for item in self.pasajeros:
            lista += ("Nombre de pasajero: " + item.nombre)
            lista += (" Apellido: " + item.apellido + "\n")
        return lista

    def pasajeroMasJoven(self):
        listaEdades = []
        for item in self.pasajeros:
            listaEdades.append(item.fechaNacimiento)
        for item in self.pasajeros:
            if item.fechaNacimiento == max(listaEdades):
                return item