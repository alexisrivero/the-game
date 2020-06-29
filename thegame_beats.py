# crear un programa que reciba por linea de comando ciertos tecleos tuyos (kerpresses) y por cada tecleo emita un sonido
# pip install <nombre>
# themes: si cambio una variable, en vez de sonar como piano, suena como soundboard de diego ferrio

from abc import ABC, abstractmethod
from playsound import playsound
import keyboard

# inicialzar pianito


class Pianito():
    tipo_sonido = ""

    def __init__(self):
        pass

    def reproducir_sonido(self, tipo_sonido, configuracion):
        self.tipo_sonido = tipo_sonido
        factory = Factory()
        nuevo_sonido = factory.crear_sonido(tipo_sonido, configuracion)
        nuevo_sonido.play()

# inicilizar tema de fondo


class BackgroundBeat():

    def __init__(self):
        playsound('beat.mp3', False)

# inicializar sonidos


class Sonido(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Snare(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('snare.mp3', False)

#    def __str__(self):
#        return "Un lindo snare"


class Kick(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('kick.mp3', False)

#    def __str__(self):
#        return "Un lindo kick"


class HiHat(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('hihat.mp3', False)

#    def __str__(self):
#        return "Un lindo jaijat"


class Bruh(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('bruh.mp3', False)

#    def __str__(self):
#        return 'un lindo bruh'


class Blaster(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('blaster.mp3', False)

#    def __str__(self):
#        return 'un lindo blaster de star barrientos'


class Cuac(Sonido):

    def __init__(self):
        pass

    def play(self):
        playsound('cuac.mp3', False)

#    def __str__(self):
#        return 'un lindo cuac'


class ConfiguracionSonidoTeclado():
    _instancia = None
    primer_sonido = None
    segundo_sonido = None
    tercer_sonido = None
    cuarto_sonido = None

    def __new__(cls):
        if ConfiguracionSonidoTeclado._instancia is None:
            ConfiguracionSonidoTeclado._instancia = object.__new__(cls)
        return ConfiguracionSonidoTeclado._instancia

    def __init__(self, primer_sonido=None, segundo_sonido=None, tercer_sonido=None, cuarto_sonido=None):
        pass

    def configurar_sonidos(self, primer_sonido, segundo_sonido, tercer_sonido, cuarto_sonido):
        self.primer_sonido = primer_sonido
        self.segundo_sonido = segundo_sonido
        self.tercer_sonido = tercer_sonido
        self.cuarto_sonido = cuarto_sonido


class Factory():

    def __init__(self):
        pass

    def crear_sonido(self, tecla, configuracion_sonido):
        self.tecla = tecla
        nuevo_sonido = None

        if self.tecla is "q":
            nuevo_sonido = configuracion_sonido.primer_sonido
        if self.tecla is "w":
            nuevo_sonido = configuracion_sonido.segundo_sonido
        if self.tecla is "e":
            nuevo_sonido = configuracion_sonido.tercer_sonido
        if self.tecla is "r":
            nuevo_sonido = configuracion_sonido.cuarto_sonido

        print("La factory devolvio un " + str(nuevo_sonido))
        return nuevo_sonido


def callback_boton_apretado(evento):
    # factory con el nombre de la tecla, que te devuelva el sonido a reproducir
    config_uno = ConfiguracionSonidoTeclado()

    if(evento.name == "k"):
        print(config_uno.primer_sonido)
        config_uno.configurar_sonidos(HiHat(), Snare(), Blaster(), Kick())
    else:
        print(config_uno.primer_sonido)
        p = Pianito()
        config_uno.configurar_sonidos(Snare(), HiHat(), Blaster(), Kick())
        p.reproducir_sonido(evento.name, config_uno)


keyboard.on_press_key('q', callback_boton_apretado)
keyboard.on_press_key('w', callback_boton_apretado)
keyboard.on_press_key('e', callback_boton_apretado)
keyboard.on_press_key('k', callback_boton_apretado)


beat = BackgroundBeat()


while True:
    pass

keyboard.unhook_all()
