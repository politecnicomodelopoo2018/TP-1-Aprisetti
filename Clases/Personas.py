class Persona(object):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.dni = dni


class Pasajeros(Persona):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None, vip = None,
                 solicitudesEspeciales = None):

        Persona.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.vip = vip
        self.solicitudesEspeciales = solicitudesEspeciales

class Tripulacion(Persona):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        Persona.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.avionesHabilitados = []

class Pilotos(Tripulacion):

    pass

class Servicio(Tripulacion):

    def __init__(self, nombre = None, apellido = None, fechaNacimiento = None, dni = None):

        Tripulacion.__init__(self, nombre, apellido, fechaNacimiento, dni)

        self.idiomas = []