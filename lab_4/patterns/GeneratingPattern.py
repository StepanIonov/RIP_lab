from abc import ABC, abstractmethod, abstractproperty

class Business_lunch(ABC):
    """
        Интерфейс Строителя объявляет создающие методы для различных частей объектов
        Продуктов.
    """
    @abstractproperty
    def lunch(self):
        """Продуктом является ланч."""
        pass

    @abstractmethod
    def add_first_dish(self):
        pass

    @abstractmethod
    def add_second_dish(self):
        pass

    @abstractmethod
    def add_salad(self):
        pass

    @abstractmethod
    def add_drink(self):
        pass

class Business_lunch_1(Business_lunch):
    """Конкретный строитель, строящий ланч первого типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._lunch = Lunch()

    @property
    def lunch(self):
        lunch = self._lunch
        return lunch

    def add_first_dish(self):
        self._lunch.add("Суп с овощами", 100)

    def add_second_dish(self):
        self._lunch.add("Котлета с пюре", 150)

    def add_salad(self):
        self._lunch.add("Салат \"Цезарь\"", 125)

    def add_drink(self):
        self._lunch.add("Компот вишнёвый", 90)

    def add_all(self):
        self.add_first_dish()
        self.add_second_dish()
        self.add_salad()
        self.add_drink()


class Business_lunch_2(Business_lunch):
    """Конкретный строитель, строящий ланч второго типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._lunch = Lunch()

    @property
    def lunch(self):
        lunch = self._lunch
        return lunch

    def add_first_dish(self):
        self._lunch.add("Солянка", 130)

    def add_second_dish(self):
        self._lunch.add("Шашлык из свинины", 225)

    def add_salad(self):
        self._lunch.add("Салат \"Овощной\"", 100)

    def add_drink(self):
        self._lunch.add("Чай чёрный", 60)

    def add_all(self):
        self.add_first_dish()
        self.add_second_dish()
        self.add_salad()
        self.add_drink()


class Lunch():
    def __init__(self):
        self.lunch = []
        self.sum = 0

    def add(self, dish, price):
        self.lunch.append(dish)
        self.sum += price

    def list_lunch(self):
        return f"{', '.join(self.lunch)}"

    def get_sum(self):
        return self.sum


if __name__ == '__main__':
    print('Заказ №1 с первого ланча')
    order = Business_lunch_1()
    order.add_first_dish()
    order.add_second_dish()
    order.add_drink()
    print(order.lunch.list_lunch())

    print('\nЗаказ №2 с первого ланча')
    order.reset()
    order.add_second_dish()
    order.add_salad()
    print(order.lunch.list_lunch())

    print('\nЗаказ №3 со второго ланча')
    order = Business_lunch_2()
    order.add_all()
    print(order.lunch.list_lunch())
