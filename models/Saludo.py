import datetime


class Saludo:
    def __init__(self, nombre):
        if nombre == "":
            self.mensaje = "Hola"
            self.nombre = "Anónimo"
        else:
            self.mensaje = "Hola, " + nombre
            self.nombre = nombre
        self.fecha = datetime.datetime.now()
