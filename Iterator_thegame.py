# el patron iterator provee una manera de acceder a los elementos de una agregacion,conjunto,coleccion de objetos secuencialmente sin exponer su implementacion, representacion. tambien pone la tarea de traversar a la iteracion en el objeto iterador
from abc import ABC, abstractmethod


class Iterator(ABC):
    def __init__(self): pass

    @abstractmethod
    def next(self): pass

    @abstractmethod
    def has_next(self): pass

    @abstractmethod
    def reverse(self): pass


class IteradorMenu(Iterator):
    _lista_items = None

    def __init__(self, lista_items):
        self._lista_items = lista_items
        print(str(self._lista_items.__len__()))

    def has_next(self):
        if self._lista_items.__len__() > 0:
            return True
        return False

    def next(self):
        return self._lista_items.pop()

    def reverse(self):
        return self._lista_items.reverse()


class MenuItem():
    _nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.precio = precio

    def get_precio(self):
        return self.precio

    def __str__(self):
        return "Este item del menu se llama " + self._nombre + " y cuesta " + str(self.precio)


class Menu():
    lista_items = []

    def __init__(self): pass

    def agregar_item(self, item: MenuItem):
        self.lista_items.append(item)

    def generar_iterador(self):
        iterador = IteradorMenu(self.lista_items)
        return iterador


class Camarero():
    _nombre = ""
    _menu = None

    def __init__(self, nombre):
        self._nombre = nombre

    def mostrar_menu(self, menu_iterable: Iterator):
        self._menu = menu_iterable
        while self._menu.has_next():
            item = self._menu.next()
            self.mostrar_item(item)

    def mostrar_item(self, menu_item: MenuItem):
        print(menu_item)


menu_de_hoy = Menu()
menu_de_hoy.agregar_item(MenuItem('Pizza', 200))
menu_de_hoy.agregar_item(MenuItem('Tarta', 120))
menu_de_hoy.agregar_item(MenuItem('Fideos', 100))
menu_de_hoy.agregar_item(MenuItem('Guiso', 150))
menu_de_hoy.agregar_item(MenuItem('Milanesa', 250))

jorge = Camarero('jORGE')
jorge.mostrar_menu(menu_de_hoy.generar_iterador())
