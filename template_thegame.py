# vos sos un maestro de la chocolatada, el patron metodo template te va a permitir definir los pasos de un algoritmo y permitir a las subclases proveer la implementacion de uno o mas pasos
from abc import ABC, abstractmethod


class Chocolatada(ABC):

    def __init__(self):
        pass

    def preparar(self):
        self.calentar_leche()
        self.mesurar_cantidad()
        self.mezclar_componentes()
        self.agregar_leche()
        self.agregar_nesquik()

    def calentar_leche(self):
        print("caliento la leche")

    @abstractmethod
    def mesurar_cantidad(self):
        pass

    def mezclar_componentes(self):
        print("mezclo los componentes")

    @abstractmethod
    def agregar_leche(self):
        pass

    @abstractmethod
    def agregar_nesquik(self):
        pass


class ChocolatadaPinamarense(Chocolatada):

    def __init__(self):
        pass

    def mesurar_cantidad(self):
        print("en pinamar hacemos este the game para mesurar ")

    def agregar_leche(self):
        print("en pinamar le agregamos mas leche bro, no somos pobres ")

    def agregar_nesquik(self):
        print("mucho nesquik, yea")


class ChocolatadaPampeana(Chocolatada):

    def __init__(self):
        pass

    def mesurar_cantidad(self):
        print("en La Pampa hacemos este the game para mesurar ")

    def agregar_leche(self):
        print("en La Pampa le agregamos mas leche bro, no somos pobres ")

    def agregar_nesquik(self):
        print("mucho nesquik Pampeano, yea")


c1 = ChocolatadaPinamarense()
c1.preparar()

c2 = ChocolatadaPampeana()
c2.preparar()
