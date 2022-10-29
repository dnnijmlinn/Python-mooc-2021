import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.ian_tarkistus'

@points('2.ian_tarkistus')
class IanTarkistusTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_viisi_ja_yli(self):
        values = "5 6 11 23 52 80".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertTrue(output[0].find("Ok, olet siis") > -1, "Tulostuksesta\n{}\nei löydy merkkijonoa 'Ok, olet siis' kun syöte on {}".
                    format(output[0], value))
                self.assertTrue(output[0].find(value + "-vuotias") > -1, "Tulostuksesta\n{}\nei löydy merkkijonoa {} kun syöte on {}".
                    format(output[0], value + "-vuotias", value))

    def test_2_nollasta_viiteen(self):
        values = "0 1 4".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertTrue(output[0].find("En usko, että osaat kirjoittaa") > -1, "Tulostuksesta\n{}\nei löydy merkkijonoa 'En usko, että osaat kirjoittaa...' kun syöte on {}".
                    format(output[0], value))

    def test_3_alle_nolla(self):
        values = "-1 -5 -11 -902".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteellä {}".format(value))

            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertTrue(output[0].find("Taitaa olla virhe") > -1, "Tulostuksesta\n{}\nei löydy merkkijonoa 'Taitaa olla virhe' kun syöte on {}".
                    format(output[0], value))
                
if __name__ == '__main__':
    unittest.main()
