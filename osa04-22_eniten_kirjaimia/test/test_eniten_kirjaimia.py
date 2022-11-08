import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.eniten_kirjaimia'
function = 'eniten_kirjainta'

def get_correct(test_case: str) -> str:
    return max([(test_case.count(x), x) for x in test_case])[1]

def f(mj):
    return f'"{mj}"'

@points('4.eniten_kirjaimia')
class EnitenKirjaimiaTest(unittest.TestCase):
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
            from src.eniten_kirjaimia import eniten_kirjainta
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä eniten_kirjainta(mjono: str)' )
        try:
            from src.eniten_kirjaimia import eniten_kirjainta
            eniten_kirjainta("abc")
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu eniten_kirjainta("abc")' )

    def test_2_paluuarvon_tyyppi(self):
        eniten_kirjainta = load(exercise, function, 'fi')
        val = eniten_kirjainta("abc")
        self.assertTrue(type(val) == str, 'Funktio eniten_kirjainta ei palauta merkkijonoa kutsuttaessa eniten_kirjainta("abc")')
    
    def test_3_yksi_sana(self):
        for test_case in ["aaabb", "aabbbbc", "abcabca","xyzxyzyyxyz", "mopopojat"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                eniten_kirjainta = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = eniten_kirjainta(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa eniten_kirjainta({f(test_case)})")

    def test_4_useampi_sana(self):
        for test_case in ["aaaa bbb ccc ddddd bbb", "appilan pappilan apupappi", "xyz xyz xyz zzzzorro"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                eniten_kirjainta = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = eniten_kirjainta(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa eniten_kirjainta({f(test_case)})")
 
if __name__ == '__main__':
    unittest.main()
