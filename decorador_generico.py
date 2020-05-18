class Decorado():
    numerito = 1

    def __init__(self):
        pass

    def metodo_cualquiera(self):
        return self.numerito


class Decorador():
    _decorado = None
    decoracion = 2

    def __init__(self, decorado):
        self._decorado = decorado

    def metodo_cualquiera(self):
        return self.decoracion + self.decorado.metodo_cualquiera()
