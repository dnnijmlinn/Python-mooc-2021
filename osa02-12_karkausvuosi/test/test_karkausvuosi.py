import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.karkausvuosi'

@points('2.karkausvuosi')
class KarkausvuosiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_neljalla_jaolliset(self):
        values = "4 16 1204 1616 1976 2008".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("on karkausvuosi") > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], "Vuosi on karkausvuosi.", value))

    def test_ei_neljalla_jaolliset(self):
        values = "5 19 1307 1753 1975 2039".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("ei ole karkausvuosi") > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], "Vuosi ei ole karkausvuosi.", value))

    def test_neljallasadalla_jaolliset(self):
        values = "400 800 1600 2000 2400".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("on karkausvuosi") > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], "Vuosi on karkausvuosi.", value))
    
    def test_sadalla_ei_400_jaolliset(self):
        values = "500 700 1100 1300 1900".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].lower().strip().find("ei ole karkausvuosi") > -1, "Tulostus\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], "Vuosi ei ole karkausvuosi.", value))
    
if __name__ == '__main__':
    unittest.main()
