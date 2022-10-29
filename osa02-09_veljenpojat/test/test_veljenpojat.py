import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.veljenpojat'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.veljenpojat')
class VeljenpojatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_mikki(self):
        values = "Mortti Vertti".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Poista otsikot
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("Mikki Hiiren veljenpoika") > -1, "Tulostuksesta {} ei löydy mainintaa 'Mikki Hiiren veljenpoika' kun syöte on {}".
                    format(output[0], value))
                self.assertFalse(output[0].find("Aku Ankan veljenpoika") > -1, "Tulostuksesta {} löytyy maininta 'Aku Ankan veljenpoika' kun syöte on {}".
                    format(output[0], value))

    def test_aku(self):
        values = "Tupu Hupu Lupu".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Poista otsikot
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))


                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("Aku Ankan veljenpoika") > -1, "Tulostuksesta {} ei löydy mainintaa 'Aku Ankan veljenpoika' kun syöte on {}".
                    format(output[0], value))
                self.assertFalse(output[0].find("Mikki Hiiren veljenpoika") > -1, "Tulostuksesta {} löytyy maininta 'Mikki Hiiren veljenpoika' kun syöte on {}".
                    format(output[0], value))

    def test_muut(self):
        values = "Antti Erkki Matti".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                # Poista otsikot
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("kenenkään tuntemani hahmon veljenpoika") > -1, "Tulostuksesta {} ei löydy mainintaa 'kenenkään tuntemani hahmon veljenpoika' kun syöte on {}".
                    format(output[0], value))
                
   
if __name__ == '__main__':
    unittest.main()
