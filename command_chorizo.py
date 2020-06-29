# tenés una moza, un cocinero, una órden de trabajo y un cliente
# crear comandos para manejar el bar
# cada command es una acción sobre un objeto
from abc import abstractmethod, ABC


class Cliente():
    orden = ""

    def __init__(self):
        pass

    def set_orden(self, orden):
        self.orden = orden

    def hacer_orden(self):
        self.orden.hacer_orden()

    def cancelar_orden(self):
        self.orden.cancelar_orden()

    def esperar_orden(self):
        # aumenta el descontento
        self.orden.esperar_orden()


class Comando(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass


class ComandoOrden(Comando):

    def __init__(self):
        pass

    def ejecutar(self):
        self.hacer_orden()

    def deshacer(self):
        # ???
        pass

    def hacer_orden(self):
        pass

    def cancelar_orden(self):
        pass

    def esperar_orden(self):
        pass


class Mozo():

    def __init__(self):
        pass

    def tomar_orden(self):
        pass

    def pasar_orden(self):
        pass

    def esperar(self):
        pass


class Cocinero():

    def __init__(self):
        pass

    def recibir_orden(self):
        pass

    def cocinar_orden(self):
        pass

    def despachar_orden(self):
        pass


cliente = Cliente()
print()
