class Sistema(object):

    __instance = None

    def __new__(cls):
        if Sistema.__instance is None
            Sistema.__instance = object.__new__(cls)
        return Sistema.__instance

    def __init__(self):

        self.listaDeVuelos = []
        self.listaDeAviones = []
        self.listaDePasajeros = []
        self.listaDeTripulacion = []

    def Nomina(self, vueloIN):