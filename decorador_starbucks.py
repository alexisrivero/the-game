# -*- coding: utf-8 -*-


class Hamburguesa():
    def __init__(self):
        pass

    def costo(self):
        pass

    def descripcion(self):
        pass


class Agregados():
    _hamburguesa = None

    def __init__(self, hamburguesa):
        self._hamburguesa = hamburguesa

    def descripcion(self):
        pass

    def costo(self):
        pass


class HamburguesaNino(Hamburguesa):
    def descripcion(self):
        return "una hamburguesa pensada para los pequeños menes"

    def costo(self):
        return 5

    def __init__(self):
        pass


class HamburguesaAdulto(Hamburguesa):
    def descripcion(self):
        return "hamburguesa para menes"

    def costo(self):
        return 10

    def __init__(self):
        pass


class QuesoCheddar(Agregados):
    def __init__(self, hamburguesa):
        self._hamburguesa = hamburguesa

    def descripcion(self):
        return self._hamburguesa.descripcion() + " con cheddar"

    def costo(self):
        return 3 + self._hamburguesa.costo()


class Lechuga(Agregados):
    def __init__(self, hamburguesa):
        self._hamburguesa = hamburguesa

    def descripcion(self):
        return self._hamburguesa.descripcion() + " con lechuga"

    def costo(self):
        return 2 + self._hamburguesa.costo()


class Tomate(Agregados):

    def __init__(self, hamburguesa):
        self._hamburguesa = hamburguesa

    def descripcion(self):
        return self._hamburguesa.descripcion() + " con tomate"

    def costo(self):
        return 2 + self._hamburguesa.costo()


class Huevo(Agregados):
    def __init__(self, hamburguesa):
        self._hamburguesa = hamburguesa

    def descripcion(self):
        return self._hamburguesa.descripcion() + " con huevo"

    def costo(self):
        return 3 + self._hamburguesa.costo()


hamburguesa_adulto = HamburguesaAdulto()
print(str(hamburguesa_adulto.costo()))
print(hamburguesa_adulto.descripcion())

hamburguesa_nino = HamburguesaNino()
print(str(hamburguesa_nino.costo()))
print(hamburguesa_nino.descripcion())

hamburguesa_adulto_con_queso = QuesoCheddar(hamburguesa_adulto)
print(str(hamburguesa_adulto_con_queso.costo()))
print(hamburguesa_adulto_con_queso.descripcion())
