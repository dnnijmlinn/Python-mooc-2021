import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_rivi'
function = 'rivi_oikein'

def get_correct(test_case: list) -> int:
    c = [(reduce((lambda x,y: x + y), test_case).count(n), n) for n in (1,2)]
    return max(c)[1] if c[0][0] != c[1][0] else 0

def p(sudoku):
    m = 'sudoku = [\n'
    j = 0
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],   # rivi {j}\n'
        j += 1
    return m +']'  

@points('5.sudoku_rivi')
class SudokuRiviTest(unittest.TestCase):
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
            from src.sudoku_rivi import rivi_oikein

        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä rivi_oikein(sudoku: list, rivi: int)')
        try:
            rivi_oikein = load(exercise, function, 'fi')
            s = sudoku = [
                [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
                [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
                [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
                [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
                [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
                [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
                [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
                [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
                [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
            ]
            rivi_oikein(s, 0)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\nrivi_oikein(sudoku, 0)')

    def test_2_paluuarvon_tyyppi(self):
        rivi_oikein = load(exercise, function, 'fi')
        s = sudoku = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
            [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
        ]
        rivi = 0
        try:
            val = rivi_oikein(s, rivi)
        except:
            self.assertFalse(True, f"Varmista että seuraava kutsu toimii\n{p(s)}\nrivi_oikein(sudoku, 0)")

        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa kutsuttaessa\n{p(s)}\nrivi_oikein(sudoku, 0)")

    def test_3_toiminnallisuus(self):
        rivi_oikein = load(exercise, function, 'fi')
        s = sudoku = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],
            [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
        ]

        for rivi in [0, 3, 4, 5 ]:
            try:
                val = rivi_oikein(s, rivi)
            except:
                self.assertFalse(True, f"Varmista että seuraava kutsu toimii\n{p(s)}\nrivi_oikein(sudoku, 0)")

            self.assertEqual(val, True, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nrivi_oikein(sudoku, {rivi})")

        for rivi in [1, 2, 6, 7, 8]:
            try:
                val = rivi_oikein(s, rivi)
            except:
                self.assertFalse(True, f"Varmista että seuraava kutsu toimii\n{p(s)}\nrivi_oikein(sudoku, 0)")

            self.assertEqual(val, False, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nrivi_oikein(sudoku, {rivi})")

if __name__ == '__main__':
    unittest.main()
