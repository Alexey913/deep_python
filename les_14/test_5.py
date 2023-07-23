
# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр. 
# Напишите 3-7 тестов unittest для данного класса.

import unittest

from Rectangle_descriptor import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        for_create_test = Rectangle(2,5)

    def test_no_change(self):
        self.assertEqual(for_create_test, msg='Тест на создание прямоугольника провален!')

if __name__ == '__main__':
    unittest.main()