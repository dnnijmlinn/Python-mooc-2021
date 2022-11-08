import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_nelio'
function = 'nelio_oikein'

def p(sudoku):
    j = 0
    m = '# sarakenumerot\n#   0  1  2  3  4  5  6  7  8\nsudoku = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],   # rivi {j}\n'
        j += 1
    return m +']' 

@points('5.sudoku_nelio')
class SudokuNelioTest(unittest.TestCase):
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
            from src.sudoku_nelio import nelio_oikein
            nelio_oikein = load(exercise, function, 'fi')
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä nelio_oikein(sudoku: list, rivi: int, sarake: int)')
        try:
            from src.sudoku_nelio import nelio_oikein
            nelio_oikein = load(exercise, function, 'fi')
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
            nelio_oikein(s, 0, 0)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\nnelio_oikein(sudoku, 0, 0)')

    def test_2_paluuarvon_tyyppi(self):
        nelio_oikein = load(exercise, function, 'fi')
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
        val = nelio_oikein(s, 0, 0)
        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa kutsuttaessa\n{p(s)}\nnelio_oikein(sudoku, 0, 0)")

    def test_3_toiminnallisuus(self):
        nelio_oikein = load(exercise, function, 'fi')
        s = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
            [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ]
        ]

        for rivi, sarake in [(0, 3), (0,6), (3,0), (3,3), (6,6)]:
            val = nelio_oikein(s, rivi, sarake)
            self.assertEqual(val, True, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nnelio_oikein(sudoku, {rivi}, {sarake})")

        for rivi, sarake in [(0, 0), (3, 6), (6, 3), (6, 0)]:
            try:
                val = nelio_oikein(s, rivi, sarake)
            except: 
                self.assertEqual(val, False, f"Varmista että seuraava toimii\n{p(s)}\nnelio_oikein(sudoku, {rivi}, {sarake})")
            self.assertEqual(val, False, f"Tulos {val} on väärin kutsuttaessa \n{p(s)}\nnelio_oikein(sudoku, {rivi}, {sarake})")

if __name__ == '__main__':
    unittest.main()
