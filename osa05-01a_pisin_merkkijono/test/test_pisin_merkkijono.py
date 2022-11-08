import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.pisin_merkkijono'
function = 'pisin'

@points('5.pisin_merkkijono')
class PisinMerkkijonoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
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
            from src.pisin_merkkijono import pisin
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä pisin(merkkijonot: list)' )
        try:
            from src.pisin_merkkijono import pisin
            pisin(["ab","a"])
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\npisin(["ab","a"])' )

    def test_2_paluuarvon_tyyppi(self):
        pisin = load(exercise, function, 'fi')
        val = pisin(["ab","a"])
        self.assertTrue(type(val) == str, f'Funktio {function} ei palauta merkkijonoa kutsulla pisin(["ab","a"])')
    
    def test_3_listat(self):
        test_cases = ("eka toka kolmas", "ab abcd abc acbdefg a abcd aa", "appelsiini omena banaani päärynä", "vesihiisi sihisi hississä")
        for tc in test_cases:
            test_case = tc.split()
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisin = load(exercise, function, 'fi')
                
                correct = max(test_case, key=lambda x : len(x))
                
                try:
                    test_result = pisin(test_case)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun lista on \n{test_case}")

                self.assertEqual(correct, test_result, f"Tulos '{test_result}' ei vastaa mallivastausta '{correct}' kun lista on {test_case}")
                
              
if __name__ == '__main__':
    unittest.main()
