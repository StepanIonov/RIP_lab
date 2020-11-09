from patterns.GeneratingPattern import Business_lunch_1, Business_lunch_2
import unittest


class sumTest(unittest.TestCase):
    def test_sum_Blunch1(self):
        order = Business_lunch_1()
        order.add_all()
        self.assertEqual(order.lunch.get_sum(), 465, "Should be 465")

    def test_sum_Blunch2(self):
        order = Business_lunch_2()
        order.add_all()
        self.assertEqual(order.lunch.get_sum(), 515, "Should be 515")

if __name__=="__main__":
    unittest.main()
