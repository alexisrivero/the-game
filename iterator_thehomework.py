# sos la asistente de bill gates y tenés que ir a hacerle las compras al supermercado
# el men te dara una lista de items y vos vas al super, las iterás y comprás, perra.
# todo usando el patrón iterator del peru
# si te animás y sos un men, implementa la compra de items en reversa, aunque no sirva para nada
from abc import ABC, abstractmethod


class Iterator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def reverse(self):
        pass


class IteradorLista(Iterator):
    _lista_items = None

    def __init__(self, lista_items):
        self._lista_items = lista_items
        print(str(self._lista_items.__len__()))

    def has_next(self):
        if self._lista_items.__len__() > 0:
            return True
        return False

    def next(self):
        return self._lista_items.pop(0)

    def reverse(self):
        return self._lista_items.reverse()


class Listaitem():
    _nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.precio = precio

    def get_precio(self):
        return self.precio

    def __str__(self):
        return "mi jefe el kinge bill gates me manda a comprar " + self._nombre + " y sale " + str(self.precio)


class Lista():
    lista_items = []

    def __init__(self):
        pass

    def agregar_item(self, item: Listaitem):
        self.lista_items.append(item)

    def invertir_lista(self):
        self.lista_items.reverse()
        print(self.lista_items)

    def generar_iterador(self):
        iterador = IteradorLista(self.lista_items)
        return iterador


class Asistente():
    _nombre = ""
    _lista = None

    def __init__(self, nombre):
        self._nombre = nombre

    def mostrar_lista(self, lista_iterable: Iterator):
        self._lista = lista_iterable
        while self._lista.has_next():
            item = self._lista.next()
            self.mostrar_item(item)

    def mostrar_item(self, lista_item: Listaitem):
        print(lista_item)


lista_de_compras = Lista()
lista_de_compras.agregar_item(Listaitem('pan', 30))
lista_de_compras.agregar_item(Listaitem('queso', 25))
lista_de_compras.agregar_item(Listaitem('jamon', 50))
lista_de_compras.agregar_item(Listaitem('hamburguesa', 150))


tino = Asistente('tino')
tino.mostrar_lista(lista_de_compras.generar_iterador())

lista_de_compras.agregar_item(Listaitem('pan', 30))
lista_de_compras.agregar_item(Listaitem('queso', 25))
lista_de_compras.agregar_item(Listaitem('jamon', 50))
lista_de_compras.agregar_item(Listaitem('hamburguesa', 150))

lista_de_compras.invertir_lista()
tino.mostrar_lista(lista_de_compras.generar_iterador())
