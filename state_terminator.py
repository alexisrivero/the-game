# t-800(arnoldo), t-1000(el groso), t-1200, t-2000
# state: permite a un objeto mantener su comportamiento cuando su estado interno cambia
from abc import ABC, abstractmethod


class Terminator(ABC):
    _modelo = ''
    _descripcion = ''

    def __init__(self, modelo, descripcion):
        self._modelo = modelo
        self._descripcion = descripcion

    def apuntar(self):
        pass

    def matar(self):
        pass

    def perseguir(self):
        pass

    def proteger(self):
        pass

    def thumbs_up(self):
        pass


class T800(Terminator):
    _modelo = ''
    _descripcion = ''
    tengo_objetivo = False
    objetivo = None
    brazo_apuntado = False
    pistola = None
    pistola_lista = False
    posicion = 0
    objetivo_en_rango = False
    APUNTANDO = 0
    CORRIENDO = 1
    DISPARANDO = 2
    DESCANSANDO = 3
    MANTENIMIENTO = 99
    estado = DESCANSANDO

    def __init__(self, modelo, descripcion):
        self._modelo = modelo
        self._descripcion = descripcion

    def tomar_objetivo(self, objetivo):
        self.objetivo = objetivo
        self.tengo_objetivo = True

    def disengage(self):
        self.objetivo = None
        self.tengo_objetivo = False

    def apuntar(self):
        if self.tengo_objetivo and self.estado is not self.DISPARANDO:
            self.mover_brazo(self.objetivo)

    def mover_brazo(self, objetivo):
        if self.tengo_objetivo and self.objetivo is objetivo and self.estado is not self.DISPARANDO and self.estado is not self.MANTENIMIENTO:
            self.brazo_apuntado = True
        else:
            self.brazo_apuntado = False

    def matar(self):
        if self.tengo_objetivo and self.brazo_apuntado and self.pistola_lista:
            if self.objetivo_en_rango:
                self.pistola.disparar()
            else:
                self.perseguir(self.objetivo)
        else:
            print("Terminator not ready to shoot")

    def perseguir(self, objetivo):
        if self.check_rango(self.objetivo) < 50:
            self.objetivo_en_rango = True
        else:
            self.mover_hacia(self.objetivo)
            self.objetivo_en_rango = False

    def check_rango(self, objetivo):
        return self.posicion - self.objetivo.get_posicion()

    def mover_hacia(self, objetivo):
        self.posicion = self.posicion + 1

    def proteger(self):
        pass

    def thumbs_up(self):
        pass
