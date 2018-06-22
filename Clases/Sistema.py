class Sistema(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Sistema.__instance is None:
            Sistema.__instance = object.__new__(cls)
        return Sistema.__instance

    def __init__(self):

        self.listaDeVuelos = []
        self.listaDeAviones = []
        self.listaDePasajeros = []
        self.listaDeTripulacion = []

    def mostrarPasajeroEnVuelo(self, vuelo):
        return vuelo.mostrarListaPasajeros()

    def mostrarPasajeroMasJovenEnVuelo(self, vuelo):
        return vuelo.pasajeroMasJoven()

    def mostrarminimaTripulacion(self, vuelo):
        try:
            return vuelo.minimaTripulacion()
        except AttributeError:
            pass

    def mostrarTripulacionNoAutorizada(self, vuelo):
        try:
            return vuelo.tripulacionNoAutorizada()
        except AttributeError:
            pass

    def tripulacionQueVuelaMasDeUnaVez(self):

        listaAux = []

        for primerVuelo in self.listaDeVuelos:
            for segundoVuelo in self.listaDeVuelos:
                if primerVuelo != segundoVuelo and primerVuelo.fecha == segundoVuelo.fecha:
                    for tripulante in primerVuelo.tripulacion:
                        if tripulante in segundoVuelo.tripulacion:
                            if tripulante not in listaAux:
                                listaAux.append(tripulante)

        return listaAux

    def mostrarPersonaEspecial(self, vuelo):
        return vuelo.personasEspeciales()

    def mostrarListaIdiomas(self, vuelo):
        return vuelo.idiomasHablados()
