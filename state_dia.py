# convertir este degame en una maquina de estados con la función 'imprimir' que muestre que día es

import datetime
from abc import ABC, abstractmethod


dia = datetime.datetime.today().weekday()

if dia == 0:
    print("Domingo")
elif dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")


class Estado(ABC):
    dia = 0

    def __init__(self):
        pass

    @abstractmethod
    def inicializar(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

    def is_dia(self, dia):
        if self.dia == dia:
            return True
        return False


class Reloj():
    estado = None
    dia = 0
    dias = None

    def __init__(self):
        self.dia = datetime.datetime.today().weekday()
        self.dias = []
        self.dias.append(EstadoDomingo(self))
        self.dias.append(EstadoMartes(self))
        self.dias.append(EstadoLunes(self))
        self.dias.append(EstadoMiercoles(self))
        self.dias.append(EstadoJueves(self))
        self.dias.append(EstadoViernes(self))
        self.dias.append(EstadoSabado(self))
        self.inicializar()

    def inicializar(self):
        for dia in self.dias:
            if dia.is_dia(self.dia):
                self.estado = dia
                break

    def mostrar(self):
        self.estado.mostrar()

#    def otra_accion(self):
#        self.estado.accion_random()


class EstadoDomingo(Estado):
    dia = 0

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es Domingo")


class EstadoLunes(Estado):
    dia = 1

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es lunes")


class EstadoMartes(Estado):
    dia = 2

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es martes")


class EstadoMiercoles(Estado):
    dia = 3

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es Miércoles")


class EstadoJueves(Estado):
    dia = 4

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es Jueves")


class EstadoViernes(Estado):

    dia = 5

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es Viernes")


class EstadoSabado(Estado):

    dia = 6

    def __init__(self, datetime):
        pass

    def inicializar(self):
        pass

    def mostrar(self):
        print("Hoy es Sábado")


relos = Reloj()
relos.mostrar()
