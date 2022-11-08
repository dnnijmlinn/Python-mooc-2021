import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.luvuista_suurin'

@points('4.luvuista_suurin')
class LuvuistaSuurinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.luvuista_suurin import luvuista_suurin
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään luvuista_suurin')
        try:
            from src.luvuista_suurin import luvuista_suurin
            luvuista_suurin(5, 3, 7)
        except:
            self.assertTrue(False, f'Varmista että funktion suoritus onnistuu seuraavasti\nluvuista_suurin(3, 5, 7)')

    def test_2_kuvio_kunnossa(self):
        for a, b, c in [(3,5,7), (9, -1, 3), (1,1,1), (4,5,5), (-1, 9, 3), (12,11, 10), (-100, 100, -200), (2,1,2), (1,1,-100), (7, 3, 5), (5,7,3), (42, 42, 42), (1, 0, -1) ]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.luvuista_suurin import luvuista_suurin
                vast = luvuista_suurin(a,b,c)
                output_all = get_stdout().replace(output_alussa, '', 1)

                self.assertFalse(vast == None, f'Funktiokutsun luvuista_suurin({a}, {b}, {c}) pitäisi palauttaa {max([a, b, c])} nyt se ei palauta mitään. Varmista, että funktiossasi käytetään return-komentoa')           
                self.assertEqual(vast, max([a, b, c]), f'Funktiokutsun luvuista_suurin({a}, {b}, {c}) pitäisi palauttaa {max([a, b, c])} nyt se palauttaa {vast}')
                self.assertFalse(len(output_all)>0, f'Funktiokutsun luvuista_suurin({a}, {b}, {c}) ei pitäisi tulostaa mitään, sen kuitenkin tulostaa\n{output_all}\npoista print-komennot metodin sisältä')

if __name__ == '__main__':
    unittest.main()
