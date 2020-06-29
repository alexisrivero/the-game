# el patron proxy provee un placeholder para otro objeto para controlar el acceso. por que? porque este objeto del cual queremos hacer un proxy puede ser remoto, caro de crear o con una necesidad de ser asegurado
# 2 tipos de proxy: 1. remote proxy: actua como un representativo local de un objeto que vive en algun otro ambiente de trabajo
#                  2. virtual proxy: actua como un representativo de un objeto que puede ser caro o costoso de crear, lo que hace es manejar la creacion del objeto cuando sea necesario y ademas delegar los pedidos directamente a esos objetos
from abc import ABC, abstractmethod


class Imagen(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_ancho(self):
        pass

    @abstractmethod
    def get_alto(self):
        pass

    @abstractmethod
    def dibujar(self):
        pass


class ArchivoImagen():
    ancho = 0
    alto = 0
    tamano = 0
    nombre = ""

    def __init__(self, nombre, url):
        if url != '':
            self.ancho = 126
            self.alto = 124
            self.tamano = 5020
            self.nombre = nombre

    def descripcion(self):
        return "Una linda imágen"


class RealImagen(Imagen):
    _imagen_lista = False
    _url = ''
    _archivo = None
    _nombre = ""

    def __init__(self, nombre):
        self._nombre = nombre

    def get_ancho(self):
        return self._archivo.ancho

    def get_alto(self):
        return self._archivo.alto

    def dibujar(self):
        if self._archivo:
            return self._archivo.descripcion()

    def obtener_imagen(self):
        self._imagen_lista = False

    def finalizar_obtencion_imagen(self):
        self._imagen_lista = True
        self._url = 'diego.com'
        print('fuí al peru y volví con la imágen')
        self._archivo = ArchivoImagen('img1', self._url)

    def esta_lista(self):
        return self._imagen_lista


class ProxyImagen(Imagen):
    _imagen = None
    _nombre = ''
    _alguna_condicion = True

    def __init__(self, nombre):
        self._nombre = nombre
        self._imagen = RealImagen(self._nombre)
        self._imagen.obtener_imagen()

    def forzar_el_peru(self):
        self._imagen.obtener_imagen()
        self._imagen.finalizar_obtencion_imagen()

    def chequear_acceso_al_peru(self):
        # aLGUNA Condición
        if self._alguna_condicion:
            return True
        return False

    def get_ancho(self):
        if self._imagen.esta_lista():
            return self._imagen.get_ancho()
        else:
            return 800

    def get_alto(self):
        if self._imagen.esta_lista():
            return self._imagen.get_alto()
        else:
            return 600

    def dibujar(self):
        if self._imagen.esta_lista() and self.chequear_acceso_al_peru():
            if self._imagen.dibujar() is not None:
                return self._imagen.dibujar()
            else:
                return "Una linda imágen que todavía no ha cargado"
        else:
            return "Una linda imágen que todavía no está lista o usted no tiene acceso atrevido"


class PartePaginaDiego():

    def __init__(self):
        pass

    def mostrar_imagen(self, imagen: Imagen):
        print(imagen.dibujar())


diego_el_rey_com = PartePaginaDiego()

cara_DE_DIEGO = ProxyImagen("cara_de_diego.png")
diego_el_rey_com.mostrar_imagen(cara_DE_DIEGO)
cara_DE_DIEGO._imagen.finalizar_obtencion_imagen()

diego_el_rey_com.mostrar_imagen(cara_DE_DIEGO)

diego_el_kinge = PartePaginaDiego()
diego_el_kinge.mostrar_imagen(cara_DE_DIEGO)

diego_o_rei = PartePaginaDiego()
cara_DE_DIEGO.forzar_el_peru()
diego_o_rei.mostrar_imagen(cara_DE_DIEGO)
