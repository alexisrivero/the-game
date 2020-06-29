# bosque > arboleda > arbol > rama > hoja
# describir cada parte de la composición
from abc import ABC, abstractmethod


class ComponenteBosque(ABC):
    _nombre = ""
    _descripcion = ""
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._parent = parent

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def remover(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def get_nombre(self):
        pass

    @abstractmethod
    def get_descripcion(self):
        pass

    def get_parent(self):
        return self._parent


class Arboleada(ComponenteBosque):
    _nombre = ""
    _descripcion = ""
    _lista_arboleada = None
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_arboleada = []
        self._parent = parent

    def agregar(self, bosque_item: ComponenteBosque):
        self._lista_arboleada.append(bosque_item)

    def remover(self, bosque_item: ComponenteBosque):
        self._lista_arboleada.remove(bosque_item)

    def mostrar(self):
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)
        for componente in self._lista_arboleada:
            componente.mostrar()

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return True


class Arbol():
    _nombre = ""
    _descripcion = ""
    _lista_arbol = None
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_arbol = []
        self._parent = parent

    def agregar(self, bosque_item: ComponenteBosque):
        self._lista_arbol.append(bosque_item)

    def remover(self, bosque_item: ComponenteBosque):
        self._lista_arbol.remove(bosque_item)

    def mostrar(self):
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)
        for componente in self._lista_arbol:
            componente.mostrar()

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return True


class Rama():
    _nombre = ""
    _descripcion = ""
    _lista_ramas = None
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_ramas = []
        self._parent = parent

    def agregar(self, bosque_item: ComponenteBosque):
        self._lista_ramas.append(bosque_item)

    def remover(self, bosque_item: ComponenteBosque):
        self._lista_ramas.remove(bosque_item)

    def mostrar(self):
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)
        for hoja in self._lista_ramas:
            hoja.mostrar()

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return True


class Hoja():
    _nombre = ''
    _descripcion = ''

    def __init__(self, nombre, descripcion):
        self._nombre = nombre
        self._descripcion = descripcion

    def mostrar(self):
        print("esta es una linda hoja verde del peru")


class Bosque(ComponenteBosque):
    _nombre = ""
    _descripcion = ""
    _lista_arboles = None
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_arboles = []
        self._parent = parent

    def agregar(self, bosque_item: ComponenteBosque):
        self._lista_arboles.append(bosque_item)

    def remover(self, bosque_item: ComponenteBosque):
        self._lista_arboles.remove(bosque_item)

    def mostrar(self):
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)
        for componente in self._lista_arboles:
            componente.mostrar()

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return True


class GuiaTuristico():

    def __init(self):
        pass

    def mostrar_bosque(self, menu: ComponenteBosque):
        menu.mostrar()

    def mostrar(self, algo):
        pass


bosque = Bosque("Bosque Pinamar", "Este es el bosque de Pinamar")
arboleada = Arboleada(
    "Arboleda Pinos", "Esta es una arboleda de pinos en el bosque de pinamar", bosque)
arbol = Arbol("Pino", "Este arbol es un pino", arboleada)
rama = Rama("Rama", "este Pino tiene ramas", arbol)

rama.agregar(Hoja("Hoja", "Las Hojas son Verdes"))
rama.agregar(Hoja("Hoja", "Las Hojas son Verdes2"))
rama.agregar(Hoja("Hoja", "Las Hojas son Verde3s"))

arbol.agregar(rama)

arboleada.agregar(arbol)

bosque.agregar(arboleada)


carloto = GuiaTuristico()
carloto.mostrar_bosque(bosque)
