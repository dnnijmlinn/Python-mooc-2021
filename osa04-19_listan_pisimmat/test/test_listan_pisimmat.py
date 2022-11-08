import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.listan_pisimmat'
function = 'pisimmat'

def get_correct(test_case: list) -> list:
    pass

@points('4.listan_pisimmat')
class ListanPisimmatTest(unittest.TestCase):
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
            from src.listan_pisimmat import pisimmat
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä pisimmat(lista: list)')
        try:
            pisimmat = load(exercise, function, 'fi')
            pisimmat(["abc", "ab"])
        except:
            self.assertTrue(False, 'Testaa funktiokutsu\npisimmat(["abc", "ab"])')


    def test_2_paluuarvon_tyyppi(self):
        pisimmat = load(exercise, function, 'fi')
        val = pisimmat(["Arto", "Matti"])
        self.assertTrue(type(val) == list, "Funktio pisimmat ei palauta listaa parametrin arvolla ['Arto', 'Matti'].")
    
    def test_3_yksi_pisin(self):
        test_cases = {("Arto", "Leena", "Santeri", "Kim", "Minna") : ["Santeri"], 
                      ("Jami", "Outi", "Magdalena", "Asko", "Toivo") : ["Magdalena"],
                      ("Serafiina", "Gandalf", "Harry", "Väiski") : ["Serafiina"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa pisimmat({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_4_monta_pisinta(self):
        test_cases = {("Arto", "Leena", "Mikko", "Kim", "Minna") : ["Leena", "Mikko", "Minna"], 
                      ("Jami", "Outi", "Rami", "Jan", "Aku", "Asko") : ["Jami", "Outi", "Rami", "Asko"],
                      ("Tupu", "Hupu", "Lupu", "Leenu", "Liinu", "Tiinu", "Jarmo") : ["Leenu", "Liinu", "Tiinu", "Jarmo"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa pisimmat({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")
          
if __name__ == '__main__':
    unittest.main()
