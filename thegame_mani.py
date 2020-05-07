# ratio de crecimiento por hoja para plantas
RATIO_CRECIMIENTO_POR_HOJA = 2.3
# ratio de crecimiento por hoja en plantas con frutos
RATIO_CRECIMIENTO_POR_HOJA_FRUTOS = 1.2


class SerVivo:
    _vida = True

    def __init__(self):
        pass

    def set_vida(self, vida):
        self._vida = vida
        print("Sólo dios puede juzgarnos")

    def get_vida(self):
        return self._vida


class Planta(SerVivo):
    nombre = ""
    _hojas = 0
    tiene_tronco = False
    meses_crecimiento = 2

    def __init__(self):
        pass

    def crecer(self):
        nuevas_hojas = self.hojas * RATIO_CRECIMIENTO_POR_HOJA
        self.hojas = self.hojas + nuevas_hojas

    def set_hojas(self, hojas):
        self.hojas = hojas

    def get_hojas(self):
        return self.hojas

    def __str__(self):
        return "Esta Planta se llama " + self.nombre + " y tiene " + str(self.hojas) + " tiene tronco" + str(self.tiene_tronco) + " y crece durante " + str(self.meses_crecimiento) + " meses"


class PlantaConFrutos(Planta):
    nombre_fruto = ""
    ratio_frutos_hojas = 0
    frutos = 0

    def __init__(self):
        pass

    def crecer(self):
        nuevas_hojas = self.hojas * RATIO_CRECIMIENTO_POR_HOJA_FRUTOS
        nuevos_frutos = self.hojas / self.ratio_frutos_hojas
        self.hojas = self.hojas + nuevas_hojas
        self.frutos = self.frutos + nuevos_frutos

    def __str__(self):
        return "Esta Planta con frutos se llama " + self.nombre + " y tiene " + str(self.hojas) + " y tiene frutas " + str(self.frutos)


aloe = Planta()
aloe.nombre = "Aloe Vera"
aloe.meses_crecimiento = 4
aloe.set_hojas(3)

print(aloe)

naranjo = PlantaConFrutos()
naranjo.nombre_fruto = "Naranja"
naranjo.nombre = "Naranjo"
naranjo.tiene_tronco = True
naranjo.ratio_frutos_hojas = 5
naranjo.set_hojas(25)

print(naranjo)

aloe.crecer()
naranjo.crecer()

print(aloe)
print(naranjo)
