import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.pidempi_jono'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.pidempi_jono')
class PidempiJonoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a', 'b']):
            cls.module = load_module(exercise, 'fi')

    def test_eka_pidempi(self):
        values = [("pupuankka", "kani"), ("python", "java"), ("makeinen", "karkki"), ("teräsmies", "zorro")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {test_case}")
                out = get_stdout()
                output = out.split("\n")  
                corr = test_case[0] + " on pidempi"
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteillä {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Ohjelmasi tulisi tulostaa vain yksi rivi syötteiden lisäksi, nyt se tulostaa {len(output)} riviä.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"Tuloste ei ole oikea syötteillä {test_case}: ohjelmasi tulostaa\n{out}\nkun oikea tuloste on\n{corr}")

    def test_toka_pidempi(self):
        values = [("eka", "toka"), ("lyhyt", "pidempi"), ("testi", "testaus"), ("xyz", "abcd")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {test_case}")
                out = get_stdout()
                output = out.split("\n")
                corr = test_case[1] + " on pidempi"
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteillä {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Ohjelmasi tulisi tulostaa vain yksi rivi syötteiden lisäksi, nyt se tulostaa {len(output)} riviä.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"Tuloste ei ole oikea syötteillä {test_case}: ohjelmasi tulostaa\n{out}\nkun oikea tuloste on\n{corr}")

    def test_yhta_pitkat(self):
        values = [("tik", "tok"), ("pekka", "liisa"), ("abcd", "abcd"), ("pupuankka", "apupunkka")]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                reload_module(self.module)
                out = get_stdout()
                output = out.split("\n")
                corr = "Jonot ovat yhtä pitkät"
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteillä {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Ohjelmasi tulisi tulostaa vain yksi rivi syötteiden lisäksi, nyt se tulostaa {len(output)} riviä.")
                self.assertTrue(sanitize(corr) == sanitize(out), f"Tuloste ei ole oikea syötteillä {test_case}: ohjelmasi tulostaa\n{out}\nkun oikea tuloste on\n{corr}")

if __name__ == '__main__':
    unittest.main()
