# agregar comportamiento de nado
# agregar comportamiento de caminata


class Pato():
    comportamiento_vocal = None
    comportamiento_vuelo = None
    comportamiento_nado = None
    comportamiento_caminata = None

    def __init__(self):
        pass

    def nadar(self):
        pass

    # método abstracto
    def mostrar(self):
        pass


class ComportamientoVocalAnimal():
    def __init__(self):
        pass

    def vocalizar(self):
        pass


class Cuac(ComportamientoVocalAnimal):
    def __init__(self):
        pass

    def vocalizar(self):
        print("cuac")


class Cuic(ComportamientoVocalAnimal):
    def __init__(self):
        pass

    def vocalizar(self):
        print("cuic")


class ComportamientoVuelo():
    def __init__(self):
        pass

    def volar(self):
        pass


class VolarConAlas(ComportamientoVuelo):
    def __init__(self):
        pass

    def volar(self):
        # hace algo
        pass


class NoVolar(ComportamientoVuelo):
    def __init__(self):
        pass

    def volar(self):
        # no hace nada
        pass


class ComportamientoNado():
    def __init__(self):
        pass

    def nadar(self):
        pass


class Patalear(ComportamientoNado):
    def __init__(self):
        pass

    def nadar(self):
        # patalea
        pass


class NoNadar(ComportamientoNado):
    def __init__(self):
        pass

    def nadar(self):
        # no nada
        pass


class ComportamientoCaminata():
    def __init__(self):
        pass

    def caminar(self):
        pass


class Caminar(ComportamientoCaminata):
    def __init__(self):
        pass

    def caminar(self):
        # camina
        pass


class Correr(ComportamientoCaminata):
    def __init__(self):
        pass

    def caminar(self):
        # corre
        pass


class NoCaminar(ComportamientoCaminata):
    def __init__(self):
        pass

    def caminar(self):
        # no camina ni corre
        pass


class PatoRojo(Pato):

    def __init__(self):
        super().__init__()
        self.comportamiento_vocal = Cuac()
        self.comportamiento_vuelo = VolarConAlas()
        self.comportamiento_nado = Patalear()
        self.comportamiento_nado = Caminar

    def mostrar(self):
        print("soy un pato rojo")


class PatoSilvestre(Pato):

    def __init__(self):
        super().__init__()
        self.comportamiento_vocal = Cuac()
        self.comportamiento_vuelo = VolarConAlas()
        self.comportamiento_nado = Patalear()
        self.comportamiento_caminata = Caminar()

    def mostrar(self):
        print("soy un pato silvestre")


class PatoDeUle(Pato):

    def __init__(self):
        super().__init__()
        self.comportamiento_vocal = Cuic()
        self.comportamiento_vuelo = NoVolar()
        self.comportamiento_nado = NoNadar()
        self.comportamiento_caminata = NoCaminar()

    def mostrar(self):
        print("soy un pato de ule")
