import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.aakkosjarjestyksessa_viimeinen'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.aakkosjarjestyksessa_viimeinen')
class AakkosjarjestysTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['0','0']):
            cls.module = load_module(exercise, 'fi')

    def test_1_eka_viimeineni(self):
        values = [("def","abc"), ("aapeli", "aalto"), ("kukkanen", "kaivo")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Poista otsikot
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[0]) > -1, "Tulostuksesta {} ei löydy aakkosjärjestyksessä jälkimmäistä sanaa {} kun syöte on {}".
                    format(output[0], valuegroup[0], format_tuple(valuegroup)))

    def test_2_toka_viimeineni(self):
        values = [("automaatti","autonominen"), ("lampi", "lempi"), ("abcde", "xyz")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Poista otsikot
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find(valuegroup[1]) > -1, "Tulostuksesta {} ei löydy aakkosjärjestyksessä jälkimmäistä sanaa {} kun syöte on {}".
                    format(output[0], valuegroup[1], format_tuple(valuegroup)))

    def test_3_samat(self):
        values = [("testi","testi"), ("kukkanen", "kukkanen"), ("abcdefg", "abcdefg")]
        for valuegroup in values:
            with patch('builtins.input', side_effect = list(valuegroup)):
                reload_module(self.module)
                # Poista otsikot
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa kyselyjen jälkeen yhden rivin sijasta {} riviä: {} syötteellä {}".format(len(output), output, format_tuple(valuegroup)))
                self.assertTrue(output[0].find("saman sanan kahdesti") > -1, "Tulostuksesta {} ei löydy mainintaa 'Annoit saman sanan kahdesti' kun syöte on {}".
                    format(output[0], format_tuple(valuegroup)))

if __name__ == '__main__':
    unittest.main()
