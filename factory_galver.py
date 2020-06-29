# simple factory de ropa
# factory de jeans y factory de camperas


class Jeans():

    def __init__(self):
        pass

    def precio(self):
        pass

    def bajar_bragueta(self):
        pass


class JeanRoto(Jeans):

    def __init__(self):
        pass

    def precio(self):
        return 1000

    def descripcion(self):
        return "jean roto de diego"

    def bajar_bragueta(self):
        pass


class JeanAjustado(Jeans):

    def __init__(self):
        pass

    def precio(self):
        return 1500

    def descripcion(self):
        return "jean ajustado de homosex"

    def bajar_bragueta(self):
        pass


class JeanSuelto(Jeans):

    def __init__(self):
        pass

    def precio(self):
        return 700

    def descripcion(self):
        return "jeans de viejo"

    def bajar_bragueta(self):
        pass


class Vendedor():
    tipo_jean = ""

    def __init__(self):
        pass

    def vender_jean(self, tipo_jean):
        self.tipo_jean = tipo_jean
        factory = RopaFactory()
        nuevo_jean = factory.crear_jean(tipo_jean)
        return nuevo_jean

    def vender_campera(self, tipo_campera):
        self.tipo_campera = tipo_campera
        factory = RopaFactory()
        nueva_campera = factory.crear_campera(tipo_campera)
        return nueva_campera


class RopaFactory():

    def __init__(self):
        pass

    def crear_jean(self, tipo_jean):
        self.tipo_jean = tipo_jean
        nuevo_jean = None

        if tipo_jean is "jean_roto":
            nuevo_jean = JeanRoto()
        elif tipo_jean is "jean_ajustado":
            nuevo_jean = JeanAjustado()
        elif tipo_jean is "jean_roto":
            nuevo_jean = JeanRoto()

        return nuevo_jean

    def crear_campera(self, tipo_campera):
        self.tipo_campera = tipo_campera
        nueva_campera = None

        if tipo_campera is "campera_de_jean":
            nueva_campera = CamperaJean()
        elif tipo_campera is "campera_parca":
            nueva_campera = CamperaParca()
        elif tipo_campera is "campera_deportiva":
            nueva_campera = CamperaDeportiva()

        return nueva_campera


vendedor = Vendedor()

nuevo_jean_ajustado = vendedor.vender_jean("jean_ajustado")
print(nuevo_jean_ajustado.descripcion())

nuevo_jean_roto = vendedor.vender_jean("jean_roto")
print(nuevo_jean_roto.descripcion())


class Camperas():

    def __init__(self):
        pass

    def precio(self):
        pass


class CamperaJean(Camperas):

    def __init__(self):
        pass

    def precio(self):
        return 1000

    def descripcion(self):
        return "campera de jean"


class CamperaParca(Camperas):

    def __init__(self):
        pass

    def precio(self):
        return 1500

    def descripcion(self):
        return "campera Parca abrigada"


class CamperaDeportiva(Camperas):

    def __init__(self):
        pass

    def precio(self):
        return 800

    def descripcion(self):
        return "campera deportiva"


nueva_campera_parca = vendedor.vender_campera("campera_parca")
print(nueva_campera_parca.descripcion())

nueva_campera_deportiva = vendedor.vender_campera("campera_deportiva")
print(nueva_campera_deportiva.descripcion())

nueva_campera_1 = vendedor.vender_campera("campera_parca")
print(nueva_campera_1)
nueva_campera_2 = vendedor.vender_campera("campera_parca")
print(nueva_campera_2)
print("####################################")
#
j1 = vendedor.vender_jean("jean_roto")
###

j1.bajar_bragueta()
