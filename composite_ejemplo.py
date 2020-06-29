# el patron composite nos permite componer objetos en estructuras de arbol para representar jerarquias completas, composite le permite a sus clientes tratar objetos inidviduales y sus composiciones de manera uniforme
from abc import ABC, abstractmethod


class ComponenteMenu(ABC):
    _nombre = ''
    _descripcion = ''
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._parent = parent

    @abstractmethod
    def agregar(self, menu_item):
        pass

    @abstractmethod
    def remover(self, menu_item):
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


class MenuItem(ComponenteMenu):
    _descripcion = ""
    _nombre = ""
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._descripcion = descripcion
        self._nombre = nombre
        self._parent = parent

    def agregar(self, menu_item: ComponenteMenu):
        print('no está soportado')

    def remover(self, menu_item: ComponenteMenu):
        print('no está soportado')

    def mostrar(self):
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return False


class Menu(ComponenteMenu):
    _descripcion = ""
    _nombre = ""
    _lista_items = None
    _parent = None

    def __init__(self, nombre, descripcion, parent=None):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_items = []
        self._parent = parent

    def agregar(self, menu_item: MenuItem):
        self._lista_items.append(menu_item)

    def remover(self, menu_item: MenuItem):
        self._lista_items.remove(menu_item)

    def mostrar(self):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Este componente se llama : " +
              self._nombre + " > " + self._descripcion)
        print("###############################################")
        for componente in self._lista_items:
            componente.mostrar()

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def es_compuesto(self):
        return True


class Asistente():
    _nombre = ""

    def __init__(self, nombre):
        self._nombre = nombre

    def mostrar_lista(self, menu: ComponenteMenu):
        menu.mostrar()


menu_principal = Menu("Principal", "Este es el menu principal")
menu_almuerzo = Menu(
    "Almuerzos", "Este es el menu de almuerzos", menu_principal)
menu_desayuno = Menu(
    "Desayunos", "Este es el menu de desayunos", menu_principal)

menu_almuerzo.agregar(MenuItem("Milanesa", "Milanesa ricarda napolitana"))
menu_almuerzo.agregar(MenuItem("Pizza", "Pizza napolitana"))
menu_almuerzo.agregar(MenuItem("Ñoquis", "ñoquis napolitana"))

menu_desayuno.agregar(MenuItem("CAfe", "asldqw mwqo owqd qowd oq"))
menu_desayuno.agregar(MenuItem("Medialuna", "asldqw mwqo owqd qowd oq"))
menu_desayuno.agregar(MenuItem("Tostada", "asldqw mwqo owqd qowd oq"))
menu_desayuno.agregar(MenuItem("Jugo", "Milanesa ricarda napolitana"))

menu_principal.agregar(menu_almuerzo)
menu_principal.agregar(menu_desayuno)
menu_principal.agregar(MenuItem("Chorizo de la casa", "A cualquier hora"))

carlos = Asistente("Carlos")
carlos.mostrar_lista(menu_desayuno.get_parent())
# carlos.mostrar_lista(menu_principal)
carlos.mostrar_lista(
    MenuItem("Item secreto especial", "no está en ningún menu"))
