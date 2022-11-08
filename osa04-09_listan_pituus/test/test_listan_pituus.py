import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.listan_pituus'

def f(lista):
    return '[' +', '.join([str(i) for i in lista]) +']' 

@points('4.listan_pituus')
class ListanPituusTest(unittest.TestCase):
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
            from src.listan_pituus import pituus
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään pituus(alkiot: list)')
        try:
            from src.listan_pituus import pituus
            lista = [1, 2, 3]
            pituus(lista)
        except:
            self.assertTrue(False, f'Varmista että seuraava funktiokutsu onnistuu pituus([1, 2, 3])')

    def test_2_toiminta_kunnossa(self):
        for lista in [[1,2,3], [1,3,67,7,4,23,1,5,7,4], [1], [], [33,4,4,5,7,43,32,1,3,6,7,7,4], [1,1,1,1,1,1,1], [0,0,1,2,3,4,5,6,7,8]]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.listan_pituus import pituus
                vast = pituus(lista)
                output_all = get_stdout().replace(output_alussa, '', 1)
                odotettu = len(lista)

                self.assertFalse(vast == None, f'Funktiokutsun pituus({f(lista)}) pitäisi palauttaa {odotettu} nyt se ei palauta mitään. Varmista, että funktiossasi käytetään return-komentoa kaikissa tilanteissa!')           
                self.assertEqual(vast, odotettu, f'Funktiokutsun pituus({f(lista)})  pitäisi palauttaa {odotettu} nyt se palauttaa {vast}')
                self.assertFalse(len(output_all)>0, f'Funktiokutsun pituus({f(lista)})  ei pitäisi tulostaa mitään, sen kuitenkin tulostaa\n{output_all}\npoista print-komennot metodin sisältä')

if __name__ == '__main__':
    unittest.main()
