# unittest_example.py
import unittest

def my_function(x, y):
    """Subtract y from x"""
    return x - y

class MyTest(unittest.TestCase):
    def test_my_function_1(self):
        self.assertEqual(my_function(7, 4), 3)
    def test_my_function_2(self):
        self.assertRaises(TypeError, my_function, [7, '4'])
if __name__ == '__main__':
    unittest.main()
