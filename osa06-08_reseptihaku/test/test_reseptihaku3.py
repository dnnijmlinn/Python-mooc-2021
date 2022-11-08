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

@points('6.reseptihaku-osa3')
class ReseptihakuOsa3Test(unittest.TestCase):
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
            
    def test_7_hae_raakaaine_funktio_olemassa(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            try:
                from src.reseptihaku import hae_raakaaine
            except Exception as ioe:
                self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä hae_raakaaine(tiedosto: str, aine: str)')
        
            try:
                hae_raakaaine("test/reseptit1.txt", "maito")
            except Exception as ioe:
                self.assertTrue(False, 'Funktiokutsu hae_raakaaine("reseptit1.txt", "maito") aiheutti virheen')

    def test_8_hae_aika_paluuarvon_tyyppi(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_raakaaine = load(exercise, function3, 'fi')
            vas =  hae_raakaaine("test/reseptit1.txt", "maito")
            taip = str(type(vas)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(vas) == list, f"Funktion {function3} pitäisi palauttaa lista (eli list-olio), nyt se palauttaa arvon {vas} joka on tyyppiä {taip}.")

    def test_9_hae_raaka_aine_1(self):
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            hae_raakaaine = load(exercise, function3, 'fi')
            vas =  hae_raakaaine("test/reseptit1.txt", "maito")
            koodi = 'hae_raakaaine("reseptit1.txt", "maito")'
            exp = """Lettutaikina, valmistusaika 15 min
Pullataikina, valmistusaika 60 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')
        
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            vas = hae_raakaaine("test/reseptit1.txt", "kananmuna")
            koodi = 'hae_raakaaine("reseptit1.txt", "kananmuna")'
            exp = """Lettutaikina, valmistusaika 15 min
Lihapullat, valmistusaika 45 min
Pullataikina, valmistusaika 60 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')
            
        with patch('builtins.input', side_effect=['reseptit1.txt']):
            vas = hae_raakaaine("test/reseptit1.txt", "wasabi")
            koodi = 'hae_raakaaine("reseptit1.txt", "wasabi")'
            exp = """Tofurullat, valmistusaika 30 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit1.txt']):
            vas = hae_raakaaine("test/reseptit1.txt", "kaardemumma")
            koodi = 'hae_raakaaine("reseptit1.txt", "kaardemumma")'
            exp = """Pullataikina, valmistusaika 60 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')

            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

    def test_9_hae_raaka_aine_2(self):
        with patch('builtins.input', side_effect=['reseptit2.txt']):
            hae_raakaaine = load(exercise, function3, 'fi')
            vas =  hae_raakaaine("test/reseptit2.txt", "vesi")
            koodi = 'hae_raakaaine("reseptit2.txt", "vesi")'
            exp = """Kookoskakku, valmistusaika 80 min
Kaurapuuro, valmistusaika 6 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit2.txt']):
            vas =  hae_raakaaine("test/reseptit2.txt", "herne")
            koodi = 'hae_raakaaine("reseptit2.txt", "herne")'
            exp = """Aloo gobi, valmistusaika 25 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')

        with patch('builtins.input', side_effect=['reseptit2.txt']):
            vas =  hae_raakaaine("test/reseptit2.txt", "voi")
            koodi = 'hae_raakaaine("reseptit2.txt", "voi")'
            exp = """Kookoskakku, valmistusaika 80 min""".split('\n')

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')            

        with patch('builtins.input', side_effect=['reseptit2.txt']):
            vas =  hae_raakaaine("test/reseptit2.txt", "juusto")
            koodi = 'hae_raakaaine("reseptit2.txt", "juusto")'
            exp = []

            self.assertEqual(len(exp), len(vas), f'Palautettujen reseptien määrä väärä kun kutsutaan {koodi}')
            for r in vas:
                self.assertTrue(r in exp, f'Palautettiin väärä resepti {r} kun kutsuttiin {koodi}\nOikea paluuarvo on {exp}')
            for r in exp:
                self.assertTrue(r in vas, f'Kun kutsuttiin {koodi}\nOlisi palautettujen reseptien joukossa pitänyt ola {r}\nPalautettiin {vas}')            

if __name__ == '__main__':
    unittest.main()
