import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.monistetut_jonot'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.monistetut_jonot')
class MonistetutJonotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a', '1']):
            cls.module = load_module(exercise, 'fi')

    def test_jonot(self):
        values = [("moi","1"),("abc",4),("xyx",7),("hei",2),("testi",6)]
        for test_case in values:
            with patch('builtins.input', side_effect = test_case):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {test_case}")
                out = get_stdout()
                output = out.split("\n")
                corr = test_case[0] * int(test_case[1])
                self.assertTrue(len(out) > 0, "Ohjelmasi ei tulosta mitään syötteillä {}".format(test_case))
                self.assertTrue(len(output) == 1, f"Ohjelmasi tulisi tulostaa vain yksi rivi syötteiden lisäksi, nyt se tulostaa {len(output)} riviä.")
                self.assertEqual(out.strip(), corr, f"Tuloste ei ole oikea syötteillä {test_case}: ohjelmasi tulostaa\n{out}\nkun oikea tuloste on\n{corr}")

if __name__ == '__main__':
    unittest.main()
