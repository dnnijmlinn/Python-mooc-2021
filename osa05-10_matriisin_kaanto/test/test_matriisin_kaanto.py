import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.matriisin_kaanto'
function = 'transponoi'

def get_correct(test_case: list) -> int:
    pass

@points('5.matriisin_kaanto')
class MatriisiTest(unittest.TestCase):
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
            from src.matriisin_kaanto import transponoi
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä transponoi(matriisi: list)')

        try:
            transponoi = load(exercise, function, 'fi')
            transponoi([[1,2],[1,2]])
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti:\ntransponoi([[1,2],[1,2]])')

    def test_2_paluuarvon_tyyppi(self):
        transponoi = load(exercise, function, 'fi')
        val = transponoi([[1,2],[1,2]])
        self.assertTrue(val == None, f"Funktion {function} ei tulisi palauttaa arvoa.")

    def test_3_matriisit_1(self):
        test_cases = (([[1,2],[1,2]], [[1,1],[2,2]]), ([[0,1,2],[0,1,2],[0,1,2]], [[0,0,0],[1,1,1],[2,2,2]]))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                transponoi = load(exercise, function, 'fi')

                test_matrix = test_case[0]
                test_matrix2 = [r[:] for r in test_case[0]]
                try:
                    transponoi(test_matrix)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun parametri on \n{test_matrix2}")

                correct = test_case[1]

                self.assertEqual(test_matrix, correct, f"Tulos \n{test_matrix} ei vastaa mallivastausta \n{correct} kun parametri on \n{test_matrix2}")

    def test_4_matriisit_2(self):
        test_cases = (([[10,100],[10,100]], [[10,10],[100,100]]), ([[2,3,4,5],[6,7,8,9],[9,8,7,6],[5,4,3,2]], [[2,6,9,5],[3,7,8,4],[4,8,7,3],[5,9,6,2]]))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                transponoi = load(exercise, function, 'fi')

                test_matrix = test_case[0]
                test_matrix2 = [r[:] for r in test_case[0]]
                try:
                    transponoi(test_matrix)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun parametri on \n{test_matrix2}")

                correct = test_case[1]

                self.assertEqual(test_matrix, correct, f"Tulos \n{test_matrix} ei vastaa mallivastausta \n{correct} kun parametri on \n{test_matrix2}")
       
if __name__ == '__main__':
    unittest.main()
