import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.tahdet'
function = 'lista_tahtina'

def get_correct(lst: list) -> str:
    return "\n".join(["*" * x for x in lst])

@points('4.lista_tahtina')
class TahdetTest(unittest.TestCase):
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
            from src.tahdet import lista_tahtina
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lista_tahtina(luvut: list)')
        try:
            from src.tahdet import lista_tahtina
            lista_tahtina([1])
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu\nlista_tahtina([1])')

    def test_2_paluuarvon_tyyppi(self):
        from src.tahdet import lista_tahtina
        val = lista_tahtina([1])
        self.assertTrue(val == None, f"Funktion {function} ei tule palauttaa mitään, nyt se palauttaa arvon tyyppiä {type(val)}")
    
    def test_3_luvut_0(self):
        test_case = [2,2]
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            from src.tahdet import lista_tahtina
            lista_tahtina(test_case)
            
            correct = get_correct(test_case)

            output_alussa = get_stdout()
            lista_tahtina(test_case)
            output = get_stdout().replace(output_alussa+'\n', '', 1)

            c_rows = len(correct.split('\n'))
            r_rows = len(output.split('\n'))
            self.assertTrue(len(output)>0, f"Funktiosi ei tulosta mitään kun kutsutaan\nlista_tahtina({test_case})")
            self.assertEqual(c_rows, r_rows, f"Tulostettujen rivien määrä on väätä testisyötteellä {test_case}. Funktiosi tulosti {r_rows} riviä, oikea määrä on {c_rows}. Tulostus oli:\n{output}\nsen piti olla:\n{correct}\nole tarkkana että et tulosta ylimääräisiä tyhiä rivejä!")
            self.assertEqual(correct, output, f"Tulos: \n{output}\nei vastaa mallivastausta \n{correct}\ntestisyötteellä {test_case}.")

if __name__ == '__main__':
    unittest.main()
