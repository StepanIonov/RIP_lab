from patterns.BehavioralPattern import *
import unittest


class sumTest(unittest.TestCase):
    def test_sum_menu(self):
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
        self.assertEqual(menu.accept(visitor1), 'visitor_for_composite_new', "Should be 'visitor_for_composite_new'")


if __name__=="__main__":
    unittest.main()