class Avion:

    def __init__(self, codigoUnico = None, cantidadDePasajerosMaxima = None, cantidadDeTripulacionNecesaria = None):

        self.codigoUnico = codigoUnico
        self.cantidadDePasajerosMaxima = cantidadDePasajerosMaxima
        self.cantidadDeTripulacionNecesaria = cantidadDeTripulacionNecesaria

    def deserealizar(self, archivoAvion):

        self.codigoUnico = archivoAvion["codigoUnico"]
        self.cantidadDePasajerosMaxima = archivoAvion["cantidadDePasajerosMaxima"]
        self.cantidadDeTripulacionNecesaria = archivoAvion["cantidadDeTripulacionNecesaria"]