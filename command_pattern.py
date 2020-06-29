# encapsula un pedido como un objeto dejando parametrizar otro objeto con distintos pedidos y soporta tambien operaciones que se pueden deshacer
from abc import abstractmethod, ABC


class ControlRemotoBerga():
    comando = None

    def __init__(self):
        pass

    def set_comando(self, comando):
        self.comando = comando

    def apretar_boton(self):
        self.comando.ejecutar()

    def apretar_boton_deshacer(self):
        self.comando.deshacer()


class Comando(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass

    def load(self):
        pass

    def store(self):
        pass


class Luz(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class LuzTinica(Luz):
    luz_prendida = False

    def __init__(self):
        pass

    def on(self):
        self.luz_prendida = True

    def off(self):
        self.luz_prendida = False

    def __str__(self):
        return "Esta luz tinica está " + str(self.luz_prendida)


class ComandoPrenderLuzTinica(Comando):
    _luz_tinica = None

    def __init__(self, luz_tinica):
        self._luz_tinica = luz_tinica

    def ejecutar(self):
        self._luz_tinica.on()

    def deshacer(self):
        self._luz_tinica.off()


class Ventilador(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def on(self):
        prendido = True

    @abstractmethod
    def off(self):
        prendido = False


class VentiladorTinico(Ventilador):
    prendido = False

    def __init__(self):
        pass

    def on(self):
        self.prendido = True

    def off(self):
        self.prendido = False

    def __str__(self):
        return "Este ventilador esta" + str(self.prendido)


class VentiladorFurioso(Ventilador):
    _rpm = 0

    def __init__(self):
        pass

    def on(self):
        self._rpm = 1200

    def off(self):
        self._rpm = 0

    def acelerar(self):
        self._rpm = self._rpm + 200

    def desacelerar(self):
        self._rpm = self._rpm - 200

    def __str__(self):
        return "Este ventilador va a " + str(self._rpm) + " RPM"


class ComandoApagarVentilador(Comando):
    _ventilador = None

    def __init__(self, ventilador):
        self._ventilador = ventilador

    def ejecutar(self):
        self._ventilador.off()

    def deshacer(self):
        self._ventilador.on()


class ComandoSubirVelocidadVentiladorFurioso(Comando):
    _ventilador_furioso = None

    def __init__(self, ventilador):
        self._ventilador_furioso = ventilador

    def ejecutar(self):
        self._ventilador_furioso.acelerar()

    def deshacer(self):
        self._ventilador_furioso.desacelerar()


luz2 = LuzTinica()
print(luz2)

control = ControlRemotoBerga()

comando_prender_luz = ComandoPrenderLuzTinica(luz2)

control.set_comando(comando_prender_luz)

ventilador_tinico = VentiladorTinico()
print(ventilador_tinico)

ventilador_furioso = VentiladorFurioso()
print(ventilador_furioso)

comando_apagar_ventilador_tinico = ComandoApagarVentilador(
    ventilador_tinico)
comando_apagar_ventilador_furioso = ComandoApagarVentilador(
    ventilador_furioso)
comando_acelerar_ventilador_furioso = ComandoSubirVelocidadVentiladorFurioso(
    ventilador_furioso)

control.set_comando(comando_acelerar_ventilador_furioso)


while True:
    control.apretar_boton()
    print(ventilador_furioso)
    control.apretar_boton_deshacer()
    print(ventilador_furioso)
