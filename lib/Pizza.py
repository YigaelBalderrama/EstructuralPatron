from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def prepare_it(self):
        pass

    def get_price(self):
        return f"The pizza order cost: {self.price}"