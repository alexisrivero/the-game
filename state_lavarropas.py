from abc import ABC, abstractmethod


class Lavarropas():
    estado = None
    estado_desagotando = None
    estado_esperando = None
    estado_apagado = None
    estado_mant = None
    estado_secando = None
    estado_lavando = None
    estado_inicializando = None

    def __init__(self):
        self.estado_apagado = EstadoApagado(self)
        self.estado_desagotando = EstadoDesagotando(self)
        self.estado_esperando = EstadoEsperandoOrdenes(self)
        self.estado_mant = EstadoMantenimiento(self)
        self.estado_inicializando = EstadoInicializando(self)
        self.estado_lavando = EstadoLavando(self)
        self.estado_secando = EstadoSecando(self)
        self.estado = self.estado_inicializando
        self.inicializar()

    def lavar(self):
        self.estado.lavar()

    def inicializar(self):
        self.estado.inicializar()
        self.estado = self.estado_esperando

    def prender_luz_mantenimiento(self):
        pass


class Estado(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def inicializar(self):
        pass

    @abstractmethod
    def lavar(self):
        pass


class EstadoLavando(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        return "yeah"


class EstadoInicializando(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        pass


class EstadoSecando(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        print("??? no gil estoy secando")

    def lavar(self):
        print("ya está lavado esto, li estoy secando")


class EstadoDesagotando(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        pass


class EstadoEsperandoOrdenes(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        pass


class EstadoApagado(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        pass


class EstadoMantenimiento(Estado):
    _lavarropas = None

    def __init__(self, lavarropas):
        self._lavarropas = lavarropas

    def inicializar(self):
        pass

    def lavar(self):
        pass
