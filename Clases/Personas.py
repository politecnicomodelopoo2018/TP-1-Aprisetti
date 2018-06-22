from datetime import *

class Persona(object):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.dni = dni

    def deserealizar(self, archivoPersona):

        self.nombre = archivoPersona["nombre"]
        self.apellido = archivoPersona["apellido"]
        self.fechaNacimiento = datetime.strptime(archivoPersona["fechaNacimiento"], "%Y-%m-%d").date()
        self.dni = archivoPersona["dni"]






class Pasajero(Persona):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None, vip = None,
                 solicitudesEspeciales = None):

        Persona.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.vip = vip
        self.solicitudesEspeciales = solicitudesEspeciales

    def deserealizar(self, archivoPersona):

        self.nombre = archivoPersona["nombre"]
        self.apellido = archivoPersona["apellido"]
        self.fechaNacimiento = datetime.strptime(archivoPersona["fechaNacimiento"], "%Y-%m-%d").date()
        self.dni = archivoPersona["dni"]
        if int(archivoPersona["vip"]) == 1:
            self.vip == archivoPersona["vip"]
        try:
            self.solicitudesEspeciales = archivoPersona["solicitudesEspeciales"]
        except KeyError:
            pass





class Tripulacion(Persona):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        Persona.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.avionesHabilitados = []

    def deserealizar(self, archivoPersona, listaAviones):
        self.nombre = archivoPersona["nombre"]
        self.apellido = archivoPersona["apellido"]
        self.fechaNacimiento = datetime.strptime(archivoPersona["fechaNacimiento"], "%Y-%m-%d").date()
        self.dni = archivoPersona["dni"]
        for item in archivoPersona["avionesHabilitados"]:
            for avion in listaAviones:
                if avion.codigoUnico == item:
                    self.avionesHabilitados.append(avion)





class Piloto(Tripulacion):

    pass




class Servicio(Tripulacion):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        Tripulacion.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.idiomas = []

    def deserealizar(self, archivoPersona):
        self.nombre = archivoPersona["nombre"]
        self.apellido = archivoPersona["apellido"]
        self.fechaNacimiento = datetime.strptime(archivoPersona["fechaNacimiento"], "%Y-%m-%d").date()
        self.dni = archivoPersona["dni"]
        for item in archivoPersona["idiomas"]:
            self.idiomas.append(item)