# usando el template method pattern, crear un método inicializar para computadoras de distintas marcas/modelos
from abc import ABC, abstractmethod


class Computador(ABC):

    def __init__(self):
        pass

    def inicializar(self):
        self.presionar_boton()
        self.activacion_bios()
        self.lectura_disco()
        self.iniciado_de_procesos()
        self.muestra_escritorio()
        self.cargan_aplicaciones()

    def presionar_boton(self):
        print("1. presiono el boton de arranque y la fuente energiza la motherboard")

    def activacion_bios(self):
        print("2. la CPU activa el BIOS que revisa, inicializa y configura los dispositivos y transfiere el mando al dispositivo de booteo o inicio")

    def lectura_disco(self):
        print("3. se leen los primeros sectores del disco duro donde se encuentra la configuracion del inicio del sistema operativo")

    @abstractmethod
    def iniciado_de_procesos(self):
        pass

    def muestra_escritorio(self):
        print("5. se inicia el explorador y se muestra el escritorio")

    @abstractmethod
    def cargan_aplicaciones(self):
        pass


class ComputadorMacintosh(Computador):

    def __init__(self):
        pass

    def iniciado_de_procesos(self):
        print("4. Macintosh inicia los procesos, comprueba e inicializa todos los dispositivos conectados a la motherboard")

    def cargan_aplicaciones(self):
        print(
            "6. finalmente, se cargan todas las aplicaciones que se inician con Macintosh")


class ComputadorIntel(Computador):

    def __init__(self):
        pass

    def iniciado_de_procesos(self):
        print("4. Windows inicia los procesos, comprueba e inicializa todos los dispositivos conectados a la motherboard")

    def cargan_aplicaciones(self):
        print("6. finalmente, se cargan todas las aplicaciones que se inician con Windows")


mac = ComputadorMacintosh()
mac.inicializar()

intel = ComputadorIntel()
intel.inicializar()
