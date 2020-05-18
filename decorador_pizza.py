class Pizza():
    def __init__(self):
        pass

    def costo(self):
        pass

    def descripcion(self):
        pass


class Topping():
    _pizza = None

    def __init__(self):
        pass

    def descripcion(self):
        pass

    def costo(self):
        pass


class PizzaMediana(Pizza):
    def descripcion(self):
        return "Una rica pizza mediana "

    def costo(self):
        return 2

    def __init__(self):
        pass


class PizzaGrande(Pizza):
    def descripcion(self):
        return "Una rica Pizza grande "

    def costo(self):
        return 4

    def __init__(self):
        pass


class Napolitana(Topping):

    def __init__(self, pizza):
        self._pizza = pizza

    def costo(self):
        return 10 + self._pizza.costo()

    def descripcion(self):
        return self._pizza.descripcion() + " napolitana "


class Anana(Topping):
    def __init__(self, pizza):
        self._pizza = pizza

    def costo(self):
        return 13 + self._pizza.costo()

    def descripcion(self):
        return self._pizza.descripcion() + " con anana "


pizza = PizzaGrande()
print(str(pizza.costo()))
print(pizza.descripcion())

pizza_napo = Napolitana(pizza)
print(str(pizza_napo.costo()))
print(pizza_napo.descripcion())

pizza_napo_anana = Anana(pizza_napo)
print(str(pizza_napo_anana.costo()))
print(pizza_napo_anana.descripcion())
