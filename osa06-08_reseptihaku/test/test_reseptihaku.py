import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.reseptihaku'

def f(d):
    return '\n'.join(d)

function1 = "hae_nimi"
function2 = "hae_aika"
function3 = "hae_raakaaine"

testdata = ["reseptit1.txt", "reseptit2.txt"]

import os
from shutil import copyfile

@points('6.reseptihaku-osa1')
class ReseptihakuOsa1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)               
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_hae_nimi_funktio_olemassa(self):
        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            try:
                from src.reseptihaku import hae_nimi
            except Exception as ioe:
                self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä hae_nimi(tiedosto: str, sana: str)')
            try:
                hae_nimi("test/reseptit1.txt", "pulla")
            except Exception as ioe:
                self.assertTrue(False, 'Funktiokutsu hae_nimi("reseptit1.txt", "pulla") aiheutti virheen')

    def test_2_hae_nimi_paluuarvon_tyyppi(self):
        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            hae_nimi = load(exercise, function1, 'fi')
            val = hae_nimi("test/reseptit1.txt", "pulla")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == list, f"Funktion {function1} pitäisi palauttaa lista (eli list-olio), nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")

    def test_3_hae_nimi_1(self):
        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            hae_nimi = load(exercise, function1, 'fi')
            vas = hae_nimi("test/reseptit1.txt", "pulla")
            koodi = 'hae_nimi("reseptit1.txt", "pulla")'
            exp = """Lihapullat
Pullataikina""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            vas = hae_nimi("test/reseptit1.txt", "tofu")
            koodi = 'hae_nimi("reseptit1.txt", "tofu")'
            exp = """Tofurullat""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            vas = hae_nimi("test/reseptit1.txt", "a")
            koodi = 'hae_nimi("reseptit1.txt", "a")'
            exp = """Lettutaikina
Lihapullat
Tofurullat
Pullataikina""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            vas = hae_nimi("test/reseptit1.txt", "taikina")
            koodi = 'hae_nimi("reseptit1.txt", "taikina")'
            exp = """Lettutaikina
Pullataikina""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

    def test_3_hae_nimi_2(self):
        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            hae_nimi = load(exercise, function1, 'fi')
            vas = hae_nimi("test/reseptit2.txt", "ka")
            koodi = 'hae_nimi("reseptit2.txt", "ka")'
            exp = """Kookoskakku
Kaurapuuro
Mansikkarahka
Mantelikala""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect = ["reseptit1.txt"]*10):
            vas = hae_nimi("test/reseptit2.txt", "alo")
            koodi = 'hae_nimi("reseptit2.txt", "alo")'
            exp = """Aloo gobi""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

if __name__ == '__main__':
    unittest.main()
