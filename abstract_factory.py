from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def emitir_sonido(self):
        pass


class Pato(Animal):
    def __init__(self):
        pass

    def emitir_sonido(self):
        return "quackerino"


p = Pato()
p.emitir_sonido()
print(p.emitir_sonido())


class FactoryIngredientesPizza(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def crear_masa(self):
        pass

    @abstractmethod
    def crear_salsa(self):
        pass

    @abstractmethod
    def crear_queso(self):
        pass

    @abstractmethod
    def crear_topping(self):
        pass


class FactoryMasaJujuy():
    tipo_masa = None

    def __init__(self):
        pass

    def crear(self, tipo_masa):
        if tipo_masa is "masa_finita":
            return MasaFinita()
        elif tipo_masa is "masa_gorda":
            return MasaGorda()


class Masa(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class MasaFinita(Masa):
    def __init__(self):
        pass

    def descripcion(self):
        return "Masa Finita"


class MasaGorda(Masa):
    def __init__(self):
        pass

    def descripcion(self):
        return "Masa Gorda"


class BA_FactoryIngredientesPizza(FactoryIngredientesPizza):
    masa_factory = None

    def __init__(self):
        self.masa_factory = FactoryMasaJujuy()
        pass

    def crear_masa(self, tipo_masa):
        return self.masa_factory.crear(tipo_masa)
