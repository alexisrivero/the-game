# hacete un proxy para subir videos a youtube desde la CIA
# SubidorVideos es de la CIA pero por dentro usamos las librerias (ficticias) de youtube.com

from abc import ABC, abstractmethod


class Video(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def duracion(self):
        pass

    @abstractmethod
    def get_ancho(self):
        pass

    @abstractmethod
    def get_alto(self):
        pass

    @abstractmethod
    def cargar(self):
        pass


class ArchivoVideo():
    duracion = 0
    alto = 0
    ancho = 0
    nombre = ""

    def __init__(self, nombre, url):
        if url != '':
            self.nombre = nombre
            self.alto = 480
            self.ancho = 320

    def descripcion(self):
        return "a nice touch by mickie"


class RealVideo(Video):
    _video_listo = False
    _url = ''
    _archivo = None
    _nombre = ""

    def __init__(self, nombre):
        self._nombre = nombre

    def get_ancho(self):
        return self._archivo.ancho

    def get_alto(self):
        return self._archivo.alto

    def cargar(self):
        if self._archivo:
            return self._archivo.descripcion()

    def obtener_video(self):
        self._video_listo = False

    def finalizar_obtencion_video(self):
        self._video_listo = True
        self._url = 'mickie.com'
        print('fui a youtube y volvi con el video')
        self._archivo = ArchivoVideo('video', self._url)

    def esta_listo(self):
        return self._video_listo


class ProxyVideo(Video):
    _video = None
    _nombre = ''
    _alguna_condicion = True

    def __init__(self, nombre):
        self._nombre = nombre
        self._video = RealVideo(self._nombre)
        self._video.obtener_video()

    def forzar_el_video(self):
        self._video.obtener_video()
        self._video.finalizar_obtencion_video()

    def chequear_acceso_al_video(self):
        if self._alguna_condicion:
            return True
        return False

    def get_ancho(self):
        if self._video.esta_listo():
            return self._video.get_ancho()
        else:
            return 500

    def get_alto(self):
        if self._video.esta_listo():
            return self._video.get_alto()
        else:
            return 400

    def cargar(self):
        if self._video.esta_listo() and self.chequear_acceso_al_video():
            if self._video.cargar() is not None:
                return self._video.cargar()
            else:
                return "El video todavia no cargo"
        else:
            return "el video no esta listo o usted no tiene acceso"


class PartePaginaCia():

    def __init__(self):
        pass

    def mostrar_video(self, video: Video):
        print(video.cargar())


cia_com = PartePaginaCia

a_nice_touch = ProxyVideo("a_nice_touch_by_mickie.mp4")
cia_com.mostrar_video(a_nice_touch)
a_nice_touch._video.finalizar_obtencion_video()

cia_com.mostrar_video(a_nice_touch)

mickie_el_kinge = PartePaginaCia()
mickie_el_kinge.mostrar_video(a_nice_touch)
