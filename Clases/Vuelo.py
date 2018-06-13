import datetime

class Vuelo:

    def __init__(self, avion = None, fecha = None, hora = None, origen = None, destino = None):

        self.avion = avion
        self.fecha = fecha
        self.hora = hora
        self.origen = origen
        self.destino = destino

        self.tripulacion = []
        self.pasajeros = []

    def deserializar(self, archivoVuelo):

        self.avion = archivoVuelo["Avion"]
        self.fecha = datetime.strptime(archivoVuelo["fecha"], "%Y-%m-%d").date()
        self.hora = archivoVuelo["hora"]
        self.origen = archivoVuelo["origen"]
        self.destino = archivoVuelo["destino"]

        for item in archivoVuelo["pasajeros"]:
            self.pasajeros.append(item)

        for item in archivoVuelo["tripulacion"]:
            self.tripulacion.append(item)
