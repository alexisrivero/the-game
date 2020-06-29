# hay un fan de la comida peruana que solo come comida peruana, pero nosotros hacemos comida paraguaya, hacer que el comensal se trague la comida peruana igual.
from abc import ABC, abstractmethod


class Comida(ABC):
    esta_rica = False

    def __init__(self):
        pass


class ComidaPeruana(Comida):
    es_picante = True
    es_colorida = True

    def __init__(self):
        pass

    def picante(self):
        return self.es_picante

    def colorida(self):
        return self.es_colorida

    def colorear_comida(self):
        self.es_colorida = True

    def picantear_comida(self):
        self.es_picante = True

    def __str__(self):
        return "La comida peruana es famosa por ser picante " + str(self.es_picante) + " y por ser colorida gracias al aji" + str(self.es_colorida)


class ComidaParaguaya(Comida):
    es_salada = True
    es_picante = True

    def __init__(self):
        pass

    def salada(self):
        return self.es_salada

    def picante(self):
        return self.es_picante

    def __str__(self):
        return "La comida paraguaya es famosa por ser salada " + str(self.es_salada) + " y por tener asados mejores " + str(self.es_picante)


class FanComidaPeruana():
    _comida_peruana = None

    def __init__(self):
        pass

    def comer(self, comida_peruana: ComidaPeruana):
        self._comida_peruana = comida_peruana
        if not self._comida_peruana.picante() or not self._comida_peruana.colorida():
            self.volver_a_pedir()
            print("vamos a salsear esta mierda")
        else:
            print("que ricardo")

    def volver_a_pedir(self):
        self._comida_peruana.colorear_comida()
        self._comida_peruana.picantear_comida()
        self.comer(self._comida_peruana)


class ComidaPeruanaAdapter(ComidaPeruana):
    _comida_paraguaya = None

    def __init__(self, comida_paraguaya: ComidaParaguaya):
        self._comida_paraguaya = comida_paraguaya

    def picante(self):
        return self._comida_paraguaya.es_picante

    def colorida(self):
        return self._comida_paraguaya.es_salada

    def colorear_comida(self):
        self._comida_paraguaya.es_colorida = True

    def picantear_comida(self):
        self._comida_paraguaya.es_salada = True

    def __str__(self):
        return "Esta comida es picante? " + str(self._comida_paraguaya.es_picante) + "y es salada? " + str(self._comida_paraguaya.es_salada)


comida_peruana = ComidaPeruana()
print(comida_peruana)

fan_comida_peruana = FanComidaPeruana()
fan_comida_peruana.comer(comida_peruana)
comida_peruana.es_picante = False
fan_comida_peruana.comer(comida_peruana)
comida_paraguaya = ComidaParaguaya()

el_enganio_trevisan = ComidaPeruanaAdapter(comida_paraguaya)


fan_comida_peruana.comer(el_enganio_trevisan)

print(comida_paraguaya)
