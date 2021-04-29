from lib.Pizza import Pizza


class Decorator(Pizza):

    _pizza_base: Pizza

    def __init__(self, pizza: Pizza):
        self._pizza_base = pizza

    @property
    def pizza(self):
        return self._pizza_base

    def prepare_it(self):
        return self._pizza_base.prepare_it()

