import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
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

@points('6.reseptihaku-osa2')
class ReseptihakuOsa2Test(unittest.TestCase):
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

    def test_4_hae_aika_funktio_olemassa(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            try:
                from src.reseptihaku import hae_aika
            except Exception as ioe:
                self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä hae_aika(tiedosto: str, aika: int)')
        
            try:
                hae_aika("test/reseptit1.txt", 20)
            except Exception as ioe:
                self.assertTrue(False, 'Funktiokutsu hae_aika("reseptit1.txt", 20) aiheutti virheen')

    def test_5_hae_aika_paluuarvon_tyyppi(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit1.txt", 20)
            taip = str(type(vas)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(vas) == list, f"Funktion {function2} pitäisi palauttaa lista (eli list-olio), nyt se palauttaa arvon {vas} joka on tyyppiä {taip}.")

    def test_6_hae_aika_1(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit1.txt", 20)
            koodi = 'hae_aika("reseptit1.txt", 20)'
            exp = """Lettutaikina, valmistusaika 15 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit1.txt", 30)
            koodi = 'hae_aika("reseptit1.txt", 30)'
            exp = """Lettutaikina, valmistusaika 15 min
Tofurullat, valmistusaika 30 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit1.txt", 60)
            koodi = 'hae_aika("reseptit1.txt", 60)'
            exp = """Lettutaikina, valmistusaika 15 min
Lihapullat, valmistusaika 45 min
Tofurullat, valmistusaika 30 min
Pullataikina, valmistusaika 60 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit1.txt", 1)
            koodi = 'hae_aika("reseptit1.txt", 1)'
            exp = []

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

    def test_6_hae_aika_2(self):
        with patch('builtins.input', side_effect=['reseptit2.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit2.txt", 10)
            koodi = ' hae_aika("reseptit2.txt", 10)'
            exp = """Kaurapuuro, valmistusaika 6 min
Mansikkarahka, valmistusaika 2 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit2.txt']):
            vas = hae_aika("test/reseptit2.txt", 30)
            koodi = 'hae_aika("reseptit2.txt", 30)'
            exp = """Kaurapuuro, valmistusaika 6 min
Mansikkarahka, valmistusaika 2 min
Aloo gobi, valmistusaika 25 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')
    
        with patch('builtins.input', side_effect=['reseptit2.txt']):
            hae_aika = load(exercise, function2, 'fi')
            vas = hae_aika("test/reseptit2.txt", 50)
            koodi = 'hae_aika("reseptit2.txt", 50)'
            exp = """Kaurapuuro, valmistusaika 6 min
Mansikkarahka, valmistusaika 2 min
Aloo gobi, valmistusaika 25 min
Mantelikala, valmistusaika 45 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

if __name__ == '__main__':
    unittest.main()
