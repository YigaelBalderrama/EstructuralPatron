from lib.Decorator import Decorator


class ExtraCheese(Decorator):

    def prepare_it(self):
        return f"{self.pizza.prepare_it()} and extra cheese"