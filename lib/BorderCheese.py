from lib.Decorator import Decorator


class BorderCheese(Decorator):

    def prepare_it(self):
        return f"{self.pizza.prepare_it()} with Cheese in the borders"
