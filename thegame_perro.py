# modelas perro con comportamientos de ladrido, nado y vuelo
class Perro():
    comportamiento_vuelo = None
    comportamiento_vocal = None
    comportamiendo_nado = None

    def __init__(self):
        pass


class ComportamientoLadrido():
    def __init__(self):
        pass

    def vocalizar(self):
        pass


class Woof(ComportamientoLadrido):
    def __init__(self):
        pass

    def vocalizar(self):
        print("woof")


class Bark(ComportamientoLadrido):
    def __init__(self):
        pass

    def vocalizar(self):
        print("bark")


class ComportamientoNado():
    def __init__(self):
        pass

    def nadar(self):
        pass


class NadarDePerrito(ComportamientoNado):
    def __init__(self):
        pass

    def nadar(self):
        # nada
        pass


class NoNada(ComportamientoNado):
    def __init__(self):
        pass

    def se_ahoga(self):
        # asopotamadre perrito
        pass


class ComportamientoVuelo():
    def __init__(self):
        pass

    def vuelo(self):
        # vuela
        pass


class NoVolar(ComportamientoVuelo):
    def __init__(self):
        pass

    def volar(self):
        # no vuela
        pass


class VolarConJetpack(ComportamientoVuelo):
    def __init__(self):
        pass

    def volar(self):
        # vuela con un jetpack atado a la espalda
        pass


class Samoyedo(Perro):

    def __init__(self):
        super().__init__()
        self.comportamiento_vocal = Woof()
        self.comportamiento_vuelo = NoVolar()
        self.comportamiendo_nado = ComportamientoNado()


class Caniche(Perro):

    def __init__(self):
        super().__init__()
        self.comportamiento_vocal = Bark()
        self.comportamiento_vuelo = VolarConJetpack()
        self.comportamiendo_nado = ComportamientoNado()
