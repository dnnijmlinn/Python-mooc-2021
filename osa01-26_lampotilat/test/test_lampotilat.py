import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize, remove_extra_whitespace
from functools import reduce
from random import randint

exercise = 'src.lampotilat'

def close(a, b):
    return abs(a-b) < 0.001

@points('1.lampotilat')
class LampotilatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_nolla(self):
        test_input = 32
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")

            self.assertFalse(output[-1].find("paleltaa") > -1, "Ohjelmasi tulosti viestin 'Paleltaa!' vaikka lämpötila celsiuksina ei ole alle nollan.")
            self.assertEqual(len(output), 1, "Ohjelmasi tulosti useamman kuin yhden rivin kun syöte on 32")
            out = output[0]
            e = "32 fahrenheit-astetta on 0.0 celsius-astetta" 
            e2= "32.0 fahrenheit-astetta on 0.0 celsius-astetta"
            self.assertTrue(sanitize(out) == sanitize(e) or sanitize(out) == sanitize(e2), f"Ohjelmasi pitäisi tulostaa\n{e}\nkun syöte on {32}, mutta se tulostaa\n{out}")
            tulos = float(remove_extra_whitespace(out).split(' ')[-2])
            self.assertTrue(close(tulos, 0.0), "Ohjelma ei muuntanut lämpötilaa oikein: lopputuloksen pitäisi olla 0.0, mutta ohjelmasi tulostaa " + output[0])

    def test_2_positiivinen(self):
        test_input = randint(33, 105)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")
            self.assertFalse(output[-1].find("paleltaa") > -1, "Ohjelmasi tulosti viestin 'Paleltaa!' vaikka lämpötila celsiuksina ei ole alle nollan. Varmista että näin ei tapahdu syötteellä {test_input}")
            self.assertEqual(len(output), 1, "Ohjelmasi tulosti useamman kuin yhden rivin")
            out = output[0]
            tulos = float(remove_extra_whitespace(out).split(' ')[-2])
            self.assertTrue(close(tulos, correct), "Ohjelma ei muuntanut lämpötilaa oikein: lopputulokset syötteellä {} pitäisi olla {}, mutta ohjelmasi tulostaa {}".format(test_input, correct, output[0]))

    def test_3_negatiivinen(self):
        test_input = randint(-50, 31)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")
            out = output[0]
            tulos = float(remove_extra_whitespace(out).split(' ')[-2])
            self.assertTrue(close(tulos, correct), "Ohjelma ei muuntanut lämpötilaa oikein: lopputulokset syötteellä {} pitäisi olla {}, mutta ohjelmasi tulostaa {}".format(test_input, correct, output[0]))
            self.assertTrue(len(output)>1, f"Ohjelmasi ei tulostanut viestiä 'Paleltaa!' vaikka lämpötila celsiuksina on alle nollan. Varmista että näin tapahtuu kun ohjelman syöte on {test_input}")
            self.assertTrue(output[1].find("paleltaa") > -1, f"Ohjelmasi ei tulostanut viestiä 'Paleltaa!' vaikka lämpötila celsiuksina on alle nollan. Varmista että näin tapahtuu kun ohjelman syöte on {test_input}")
   
if __name__ == '__main__':
    unittest.main()
