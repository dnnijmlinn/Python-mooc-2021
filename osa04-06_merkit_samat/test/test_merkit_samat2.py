import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.merkit_samat'

@points('4.merkit_samat')
class MerkitSamatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_5_toiminta_kunnossa(self):
        for mj, a, b in [("koodari",1,2), ("koodari",1,3), ("koodari",1,10), ("ohjelmointi",6,0),  ("ohjelmointi",10,0),  ("ohjelmointi",1,2), ("aaaa", 1, 2),  ("abracadabra", 0, 3), ("abracadabra", 0, 4), ("simsalabim", 1, 8),  ("simsalabim", 4, 5),  ("abc", 0, 3), ("simsalabim", 4, 6)]:
            with patch('builtins.input', side_effect=["2"] * 10):
                reload_module(self.module)
                output_alussa = get_stdout()
                from src.merkit_samat import samat
                try:
                    vast = samat(mj, a,b)
                except:
                    self.assertTrue(False, f'Varmista, että funktiokutsun samat("{mj}", {a}, {b}) toimii')

                output_all = get_stdout().replace(output_alussa, '', 1)
                odotettu = -1 < a < len(mj) and -1 < b < len(mj) and mj[a] == mj[b]

                self.assertFalse(vast == None, f'Funktiokutsun samat("{mj}", {a}, {b}) pitäisi palauttaa {odotettu} nyt se ei palauta mitään. Varmista, että funktiossasi käytetään return-komentoa kaikissa tilanteissa!')           
                self.assertEqual(vast, odotettu, f'Funktiokutsun samat("{mj}", {a}, {b})  pitäisi palauttaa {odotettu} nyt se palauttaa {vast}')
                self.assertFalse(len(output_all)>0, f'Funktiokutsun samat("{mj}", {a}, {b})  ei pitäisi tulostaa mitään, sen kuitenkin tulostaa\n{output_all}\npoista print-komennot metodin sisältä')

if __name__ == '__main__':
    unittest.main()
