# modelar una clase para poder representar una ferrari f-chorizo y un tanque de guerra
# vehiculos > terrestre > auto
# vehiculos > terrestre > tanque
# vehiculos > terrestre > grua


class Vehiculo:
    _motor = True

    def __init__(self):
        pass

    def set_motor(self, motor):
        self._motor = motor
        print("sino como va a arrancar broder?")

    def get_motor(self):
        return self._motor


class Terrestre(Vehiculo):
    _terrestre = True

    def __init__(self):
        pass

    def set_terrestre(self, terrestre):
        self._terrestre = terrestre
        print("este anda por el piso broder")

    def get_terrestre(self):
        return self._terrestre


class Auto(Terrestre):
    modelo_auto = ""
    cantidad_ruedas = 4
    color_auto = ""
    velocidad_maxima = 200

    def __init__(self):
        pass

    def __str__(self):
        return "Este auto es un " + self.modelo_auto + " tiene " + str(self.cantidad_ruedas) + " ruedas " + "es de color " + self.color_auto + " y alcanza una velocidad de " + str(self.velocidad_maxima) + " km/h"


class Tanque(Terrestre):
    modelo_tanque = ""
    color_tanque = ""
    velocidad_maxima = 70

    def __init__(self):
        pass

    def __str__(self):
        return "Este tanque es modelo " + self.modelo_tanque + " es de color " + self.color_tanque + " y alcanza una velocidad maxima de " + str(self.velocidad_maxima) + " km/h"


auto = Auto()
auto.modelo_auto = "Ferrari F12"
auto.color_auto = "negro"
auto.velocidad_maxima = 300

print(auto)

tanque = Tanque()
tanque.modelo_tanque = "T-90A"
tanque.color_tanque = "Camuflado Verde"
tanque.tiene_oruga = True
tanque.tiene_escotilla = True
tanque.tiene_cañon = True

print(tanque)
