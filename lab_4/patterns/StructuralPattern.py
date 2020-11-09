from abc import ABC, abstractmethod
from patterns.GeneratingPattern import Business_lunch_1, Business_lunch_2


class Component(ABC):
    """
        Базовый класс Компонент объявляет общие операции как для простых, так и для
        сложных объектов структуры.
    """
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Leaf(Component):
    """Конечный объект, не имеющий вложенных."""
    def __init__(self, value, price):
        self._value = value
        self._price = price

    def operation(self):
        return self._value

    def get_price(self):
        return self._price


class Composite(Component):
    """Объект, имеющий вложенные объекты."""
    def __init__(self, name):
        self._children = []
        self._name = name

    def add(self, component):
        self._children.append(component)
        component.parent = self

    def remove(self, component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return self._name+f"({'+'.join(results)})"

    def get_price(self):
        count = 0
        for child in self._children:
            count += child.get_price()
        return count


def client_code(component):
    print(f"Структура: {component.operation()}")
    print(f'Общая стоимость: {component.get_price()}', end='\n\n')


if __name__=='__main__':
    menu = Composite('Меню')
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

    client_code(menu)
    client_code(business_lunches)
    client_code(white_bread)
    client_code(drinks)
