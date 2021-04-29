from lib.ClassicPizza import ClassicPizza
from lib.BorderCheese import BorderCheese
from lib.ExtraCheese import ExtraCheese
from lib.Pizza import Pizza


def client(pizza: Pizza):
    return f"I have {pizza.prepare_it()}"


def main():
    normal_pizza = ClassicPizza()
    print(client(normal_pizza))
    cheese_pizza = ExtraCheese(normal_pizza)
    print(client(cheese_pizza))
    border_decorated_pizza = BorderCheese(cheese_pizza)
    print(client(border_decorated_pizza))

main()