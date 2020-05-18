# Simple Factory Pattern
class Pizza():

    def __init__(self):
        pass

    def hornear(self):
        pass

    def precio(self):
        pass

    def encajar(self):
        pass

    def descripcion(self):
        pass


class Napolitana(Pizza):

    def __init__(self):
        pass

    def precio(self):
        return 3

    def descripcion(self):
        return "Una rica pizza napolitana "


class CuatroQuesos(Pizza):

    def __init__(self):
        pass

    def precio(self):
        return 6

    def descripcion(self):
        return "Una rica pizza cuatroque "


class Fugazzeta(Pizza):
    def __init__(self):
        pass

    def precio(self):
        return 3

    def descripcion(self):
        return "Una rica pizza fugazzeta "


class PreparadorDePizza():
    tipo_pizza = ""

    def __init__(self):
        pass

    def preparar_pizza(self, tipo_pizza):
        self.tipo_pizza = tipo_pizza
        factory = PizzaFactory()
        nueva_pizza = factory.crear_pizza(tipo_pizza)
        nueva_pizza.encajar()
        return nueva_pizza


class PizzaFactory():

    def __init__(self):
        pass

    def crear_pizza(self, tipo_pizza):
        self.tipo_pizza = tipo_pizza
        nueva_pizza = None

        if tipo_pizza is "napolitana":
            nueva_pizza = Napolitana()
        elif tipo_pizza is "fugazzeta":
            nueva_pizza = Fugazzeta()
        elif tipo_pizza is "cuatro_quesos":
            nueva_pizza = CuatroQuesos()

        nueva_pizza.hornear()
        return nueva_pizza


preparador = PreparadorDePizza()

nueva_pizza_napo = preparador.preparar_pizza("napolitana")
print(nueva_pizza_napo.descripcion())

nueva_pizza_fugazetta = preparador.preparar_pizza("fugazetta")
print(nueva_pizza_fugazetta.descripcion())
