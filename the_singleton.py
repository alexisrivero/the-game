# es el patron que usamos cuando necesitamos que una clase sea instanciada una sola vez
from abc import abstractmethod, ABC


class Game(ABC):
    def __init__(self):
        pass


class Valorant(Game):
    def __init__(self):
        pass


class MotorGrafico():
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando motor gráfico")
            cls._instancia = super(MotorGrafico, cls).__new__(cls)
        return cls._instancia

    def calcular_movimientos(self):
        pass

    def dibujar_en_pantalla(self):
        pass


class Maquina():
    __instancia = None

    def __new__(cls):
        if Maquina.__instancia is None:
            Maquina.__instancia = object.__new__(cls)
        return Maquina.__instancia


class Diego():
    class _Diego():

        def __init__(self):
            pass

    __instancia = None

    def __init__(self):
        if not Diego.__instancia:
            Diego.__instancia = Diego._Diego()

    def getInstancia(self):
        return self.__instancia


class SingletonDecorator():

    def __init__(self, clase):
        self.clase = clase
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.clase(*args, **kwds)
        return self.instance


# iniciamos el juego
foo = SingletonDecorator(Valorant)

while True:
    game = foo()
    print(foo.instance)
