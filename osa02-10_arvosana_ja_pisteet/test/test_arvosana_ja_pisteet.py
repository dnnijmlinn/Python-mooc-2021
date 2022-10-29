import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.arvosana_ja_pisteet'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def get_grade(p : int) -> str:
    if p == 100:
        return "5"
    return str((p - 50) // 10 + 1)

@points('2.arvosana_ja_pisteet')
class ArvosanaJaPisteetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_negatiiviset(self):
        values = [str(randint(-1000,-1)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("mahdotonta!") > -1, "Tulostuksesta\n{}\nei löydy mainintaa 'mahdotonta!' kun syöte on {}".
                    format(output[0], value))

    def test_2_liian_suuret(self):
        values = [str(randint(101,10000)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("mahdotonta!") > -1, "Tulostuksesta\n{}\nei löydy mainintaa 'mahdotonta!' kun syöte on {}".
                    format(output[0], value))

    def test_3_hylatyt(self):
        values = [str(randint(0,49)) for i in range(5)]
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertTrue(output[0].find("hylätty") > -1, "Tulostuksesta\n{}\nei löydy mainintaa 'hylätty' kun syöte on {}".
                    format(output[0], value))

    def test_0_arvosanat(self):
        values = "50 55 59 60 67 69 70 79 80 89 90 99 100".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))

                correct = "Arvosana: " + get_grade(int(value))
                self.assertEqual(output[0].strip(), correct, "Tuloste\n{}\nei vastaa oikeaa tulostetta\n{}\nkun syöte on {}".
                    format(output[0], correct, value))
                
if __name__ == '__main__':
    unittest.main()
