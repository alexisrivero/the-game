from abc import abstractmethod, ABC


class Animal(ABC):
    esta_vivo = True

    def __init__(self):
        pass


class Pato(Animal):
    puede_volar = True
    puede_cuaquear = True

    def __init__(self):
        pass

    def volar(self):
        if not self.puede_volar:
            return False
        return True

    def cuaquear(self):
        if not self.puede_cuaquear:
            return False
        return True

    def regenerar_alas(self):
        self.puede_volar = True

    def regenerar_pico(self):
        self.puede_cuaquear = True

    def __str__(self):
        return "Este pato vuela? " + str(self.puede_volar) + " y cuaquea? " + str(self.puede_cuaquear)


class Ganso(Animal):
    puede_volar = True
    puede_gansear = True

    def __init__(self):
        pass

    def volar(self):
        if not self.puede_volar:
            return False
        return True

    def gansear(self):
        if not self.puede_gansear:
            return False
        return True

    def __str__(self):
        return "Este ganso vuela? " + str(self.puede_volar) + " y gansea? " + str(self.puede_gansear)


class VeterinarioPato():
    _pato = None

    def __init__(self):
        pass

    def atender(self, pato: Pato):
        self.pato = pato
        if not pato.volar() or not pato.cuaquear():
            self.curar(pato)

    def curar(self, pato: Pato):
        pato.regenerar_alas()
        pato.regenerar_pico()


class PatoAdapter(Pato):
    _ganso = None
    puede_volar = True
    puede_cuaquear = False

    def __init__(self, ganso: Ganso):
        self._ganso = ganso

    def cuaquear(self):
        if not self._ganso.puede_gansear:
            return False
        return True

    def volar(self):
        if not self._ganso.puede_volar:
            return False
        return True

    def regenerar_alas(self):
        self._ganso.puede_volar = True

    def regenerar_pico(self):
        self._ganso.puede_gansear = True

    def __str__(self):
        return "Este ganso vuela? " + str(self._ganso.puede_volar) + " y gansea? " + str(self._ganso.puede_gansear)


donald = Pato()
donald.puede_volar = False


veterinario_juan = VeterinarioPato()
veterinario_juan.atender(donald)

el_buen_ganso = Ganso()

el_buen_ganso.puede_gansear = False
el_buen_disfraz_de_pato = PatoAdapter(el_buen_ganso)
print(el_buen_ganso)

veterinario_juan.atender(el_buen_disfraz_de_pato)

print(el_buen_ganso)
