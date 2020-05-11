# modelar una clase para poder representar una ferrari f-chorizo y un tanque de guerra
# vehiculos > terrestre > auto
# vehiculos > terrestre > tanque
# vehiculos > terrestre > grua


class Vehiculo:
    _motor = True
    altura_al_piso = 0
    velocidad = 0
    color_chasis = "negro"
    marca = ""
    modelo = ""

    def __init__(self):
        pass

    def set_motor(self, motor):
        self._motor = motor
        print("sino como va a arrancar broder?")

    def get_motor(self):
        return self._motor


class Terrestre(Vehiculo):
    _terreno_preferido = None

    def __init__(self):
        self.altura_al_piso = 1

    def set_terreno_preferido(self, terreno):
        self._terreno_preferido = terreno

    def get_terreno_preferido(self):
        return self._terreno_preferido

    def __str__(self):
        return "Este vehiculo terrestre es un " + self.marca + "/" + self.modelo + "es de color " + self.color_chasis + " y alcanza una velocidad de " + str(self.velocidad) + " km/h"


class Auto(Terrestre):
    cantidad_ruedas = 4

    def __init__(self):
        self.velocidad = 200
        self.set_terreno_preferido("asfalto")

    def __str__(self):
        return super().__str__() + " tiene " + str(self.cantidad_ruedas) + " ruedas"
    # setters y getters para todas las propiedades


class Tanque(Terrestre):

    def __init__(self):
        self.set_terreno_preferido("cualquiera")

    def __str__(self):
        return super().__str__() + " y tiene una oruga"


auto = Auto()
auto.marca = "Ferrari"
auto.modelo = "F12"
auto.color_chasis = "negro"
auto.velocidad = 300

print(auto)

tanque = Tanque()
tanque.marca = "Panzer"
tanque.modelo = "Scheuhfefuwfufa"
tanque.color_chasis = "verde"
tanque.velocidad = 120
print(tanque)
