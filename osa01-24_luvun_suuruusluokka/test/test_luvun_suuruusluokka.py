import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.luvun_suuruusluokka'

@points('1.luvun_suuruusluokka')
class LuvunSuuruusluokkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        luku = 9
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0].strip(), "Luku on pienempi kuin 1000", "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 1000\nLuvulle " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 100\nLuvulle " + str(luku))
                self.assertEqual(output[1].strip(), "Luku on pienempi kuin 100", "Ohjelmasi ei tulostanut\nluku on pienempi kuin 100\nLuvulle " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 10\nLuvulle " + str(luku))
                self.assertEqual(output[2].strip(), "Luku on pienempi kuin 10", "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 10\nLuvulle " + str(luku))
            self.assertEqual(output[-1], "Kiitos!", "Ohjelmasi ei tulostanut lopuksi riviä 'Kiitos!'")

    def test_tulostus_2(self):
        luku = 97
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Luku on pienempi kuin 1000", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 1000 luvulle " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 100\nLuvulle " + str(luku))
                self.assertEqual(output[1], "Luku on pienempi kuin 100", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 100 luvulle " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 10\nLuvulle " + str(luku))
                self.assertEqual(output[2], "Luku on pienempi kuin 10", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 10 luvulle " + str(luku))
            self.assertEqual(output[-1], "Kiitos!", "Ohjelmasi ei tulostanut lopuksi riviä 'Kiitos!'")

    def test_tulostus_3(self):
        luku = 451
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Luku on pienempi kuin 1000", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 1000 luvulle " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 100\nLuvulle " + str(luku))
                self.assertEqual(output[1], "Luku on pienempi kuin 100", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 100 luvulle " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 10\nLuvulle " + str(luku))
                self.assertEqual(output[2], "Luku on pienempi kuin 10", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 10 luvulle " + str(luku))
            self.assertEqual(output[-1], "Kiitos!", "Ohjelmasi ei tulostanut lopuksi riviä 'Kiitos!'")

    def test_tulostus_4(self):
        luku = 111234
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Luku on pienempi kuin 1000", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 1000 luvulle " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 100\nLuvulle " + str(luku))
                self.assertEqual(output[1], "Luku on pienempi kuin 100", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 100 luvulle " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Ohjelmasi ei tulostanut\nLuku on pienempi kuin 10\nLuvulle " + str(luku))
                self.assertEqual(output[2], "Luku on pienempi kuin 10", "Ohjelmasi ei tulostanut, että luku on pienempi kuin 10 luvulle " + str(luku))
            self.assertEqual(output[-1], "Kiitos!", "Ohjelmasi ei tulostanut lopuksi riviä 'Kiitos!'")

if __name__ == '__main__':
    unittest.main()
