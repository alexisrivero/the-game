class Megafono:
    volumen = 50

    def __init__(self):
        print("MEGAFONO inicializado")
        print("Volumen iniciado en " + str(self.volumen))

    def set_volumen(self, volumen):
        if volumen > 100:
            print('volumen maximo 100 piyo')
            self.volumen = 100
        else:
            print('volumen seteado a ' + str(volumen))
            self.volumen = volumen


class MegafonoPolicial(Megafono):
    def __init__(self):
        self.volumen = 70
        super().__init__()
        print("Version Policial")

    def set_volumen(self, volumen):
        self.volumen = volumen
        print('volumen seteado a ' + str(volumen))


z = Megafono()
z.set_volumen(120)

chorizo = MegafonoPolicial()
chorizo.set_volumen(129)
