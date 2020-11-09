from patterns.StructuralPattern import Composite, Component, Leaf, client_code
from patterns.GeneratingPattern import Business_lunch_1, Business_lunch_2
from abc import ABC, abstractmethod


class ComponentNew(Component):
    """
        Интерфейс Компонента объявляет метод accept, который в качестве аргумента
        может получать любой объект, реализующий интерфейс посетителя.
    """
    @abstractmethod
    def accept(self, visitor):
        pass

class CompositeNew(Composite, ComponentNew):
    def accept(self, visitor):
        visitor.visit_component(self)
        return 'visitor_for_composite_new'

class Visitor(ABC):
    @abstractmethod
    def visit_component(self, element):
        pass

class Visitor1(Visitor):
    def visit_component(self, element):
        print('Стоимость: {}'.format(element.get_price()))

class Visitor2(Visitor):
    def visit_component(self, element):
        client_code(element)


if __name__ == '__main__':
    menu = CompositeNew('Меню')
    drinks = Composite('Напитки')
    drinks.add(Leaf('Фруктовый сок', 100))
    drinks.add(Leaf('Чай чёрный', 50))
    business_lunches = Composite('Бизнес ланчи')
    lunch1 = Business_lunch_1()
    lunch1.add_all()
    lunch2 = Business_lunch_2()
    lunch2.add_all()
    business_lunches.add(Leaf(lunch1.lunch.list_lunch(), lunch1.lunch.get_sum()))
    business_lunches.add(Leaf(lunch2.lunch.list_lunch(), lunch2.lunch.get_sum()))
    white_bread = Leaf('Белый хлеб', 15)

    menu.add(drinks)
    menu.add(business_lunches)
    menu.add(white_bread)

    visitor1 = Visitor1()
    visitor2 = Visitor2()
    print("Первый посетитель:")
    menu.accept(visitor1)
    print("\nВторой посетитель:")
    menu.accept(visitor2)
