import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_sarake'
function = 'sarake_oikein'

def get_correct(test_case: list) -> int:
    c = [(reduce((lambda x,y: x + y), test_case).count(n), n) for n in (1,2)]
    return max(c)[1] if c[0][0] != c[1][0] else 0

def p(sudoku):
    m = '# sarakenumerot\n#   0  1  2  3  4  5  6  7  8\nsudoku = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],\n'
    return m +']' 

@points('5.sudoku_sarake')
class SudokuSarakeTest(unittest.TestCase):
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
            from src.sudoku_sarake import sarake_oikein
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä sarake_oikein(sudoku: list, sarake: int)')
        try:
            sudoku_sarake = load(exercise, function, 'fi')
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
            sudoku_sarake(s, 0)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\nsarake_oikein(sudoku, 0)')

    def test_2_paluuarvon_tyyppi(self):
        sarake_oikein = load(exercise, function, 'fi')
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
        val = sarake_oikein(s, 0)
        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa kutsuttaessa\n{p(s)}\nsarake_oikein(sudoku, 0)")

    def test_3_toiminnallisuus(self):
        sarake_oikein = load(exercise, function, 'fi')
        s = sudoku = [
            [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
            [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
            [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
            [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
        ]

        for rivi in [3, 4, 7]:
            val = sarake_oikein(s, rivi)
            self.assertEqual(val, True, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nsarake_oikein(sudoku, {rivi})")

        for rivi in [0, 1, 2, 6, 8]:
            try:
                val = sarake_oikein(s, rivi)
            except:
                self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti{p(s)}\nsarake_oikein(sudoku, {rivi})')
            self.assertEqual(val, False, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nsarake_oikein(sudoku, {rivi})")

if __name__ == '__main__':
    unittest.main()
