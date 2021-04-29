from lib.Pizza import Pizza


class ClassicPizza(Pizza):

    def __init__(self):
        super().__init__()

    def prepare_it(self):
        return f"a pizza with Sauce, Chesse"