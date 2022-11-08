import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.ristinolla'
function = 'pelaa_siirto'

def get_correct(test_case: list) -> int:
    pass

def get_test_case(x: int, y: int, sign = ""):
    board = [['','',''],['','',''],['','','']]
    for i in range(randint(3,8)):
        board[randint(0,2)][randint(0,2)] = choice(('X','O'))
        
    if 0<=x<=2 and 0<=y<=2:
        board[y][x] = sign
    return board 

def kopy(b):
    c = []
    for r in b:
        c.append(r[:])
    return c

@points('5.ristinolla')
class GoTest(unittest.TestCase):
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
            from src.ristinolla import pelaa_siirto
        except:
            self.assertTrue(False, "Koodistasi pitäisi löytyä funktio nimeltä pelaa_siirto(lauta: list, x: int, y: int, nappula: str)")
        try:
            pelaa_siirto = load(exercise, function, 'fi')
            pelaa_siirto([['','',''],['','',''],['','','']], 0, 0, 'X')
        except:
            self.assertTrue(False, "Tarkista että funktiota voi kutsua seuraavasti\npelaa_siirto([['','',''],['','',''],['','','']], 0, 0, 'X')")


    def test_2_paluuarvon_tyyppi(self):
        pelaa_siirto = load(exercise, function, 'fi')
        val = pelaa_siirto([['','',''],['','',''],['','','']], 0, 0, 'X')
        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa parametrin arvoilla [['','',''],['','',''],['','','']], 0, 0, 'X'.")
    
    def test_3_vapaat_ruudut(self):
        test_cases = ((0,0,"X"), (1,1,"O"), (2,2,"X"), (0,1,"X"), (1,0,"O"), (1,2,"X"), (2,1,"O"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pelaa_siirto = load(exercise, function, 'fi')

                test_board = get_test_case(test_case[0], test_case[1], "")
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)

                board_after[test_case[1]][test_case[0]] = test_case[2]
                correct = True

                test_result = pelaa_siirto(test_board, test_case[0], test_case[1], test_case[2])

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"Matriisin tila \n{test_board}\nei vastaa mallivastausta \n{board_after}\nkun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

    def test_4_varatut_ruudut(self):
        test_cases = ((0,0,"X"), (1,1,"O"), (2,2,"X"), (0,1,"X"), (1,0,"O"), (1,2,"X"), (2,1,"O"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pelaa_siirto = load(exercise, function, 'fi')

                test_board = get_test_case(test_case[0], test_case[1], test_case[2])
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)
                correct = False

                try:
                    test_result = pelaa_siirto(test_board, test_case[0], test_case[1], test_case[2])
                except:
                    self.assertTrue(False, f"Varmista että voit kutsua funktiota parametreilla\n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"Matriisin tila \n{test_board}\nei vastaa mallivastausta \n{board_after}\nkun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

    def test_5_epavalidit_ruudut(self):
        test_cases = ((3,0,"X"), (1,11,"O"), (2,-1,"X"), (1,3,"X"), (-1,1,"X"))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pelaa_siirto = load(exercise, function, 'fi')

                test_board = get_test_case(test_case[0], test_case[1], test_case[2])
                test_board2 = kopy(test_board)
                board_after = kopy(test_board)
                correct = False

                try:
                    test_result = pelaa_siirto(test_board, test_case[0], test_case[1], test_case[2])
                except:
                    self.assertFalse(True, f"Varmista että funktiota voi kutsua parametreilla \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")
                self.assertEqual(test_board, board_after, f"Matriisin tila \n{test_board}\nei vastaa mallivastausta \n{board_after}\nkun parametrit ovat \n{test_board2}, {test_case[0]}, {test_case[1]}, {test_case[2]}")

if __name__ == '__main__':
    unittest.main()
