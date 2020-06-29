# el patron singleton asegura que una clase tiene solo una instancia y provee un unico y global punto de acceso

# feed de red social
from abc import abstractmethod, ABC


class RedSocial(ABC):
    def __init__(self):
        pass


class Facebook(RedSocial):
    def __init__(self):
        pass


class Maquina():
    _instancia = None

    def __new__(cls):
        if Maquina._instancia is None:
            Maquina._instancia = object.__new__(cls)
        return Maquina._instancia

    def cargar_fotos(self):
        pass

    def cargar_posts(self):
        pass


diego = Maquina()

while True:
    game = diego
    print(diego._instancia)
