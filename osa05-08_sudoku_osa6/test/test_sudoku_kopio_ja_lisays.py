import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint, shuffle

exercise = 'src.sudoku_kopio_ja_lisays'
function1 = 'kopioi_ja_lisaa'

def p(sudoku):
    j = 0
    m = 's = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],\n'
        j += 1
    return m +']' 

@points('5.sudoku_kopio_ja_lisays')
class SudokuKopioJaLisaysTest(unittest.TestCase):
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

    def test_1_funktio_lisays_olemassa(self):
        try:
            from src.sudoku_kopio_ja_lisays import kopioi_ja_lisaa
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä kopioi_ja_lisaa(sudoku: list, rivi: int, sarake: int, luku: int)')
     
        try:
            kopioi_ja_lisaa = load(exercise, function1, 'fi')
            s = [
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
            kopioi_ja_lisaa(s, 0, 1, 3)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\nkopioi_ja_lisaa(s, 0, 1, 3)')
     
    def test_2_funktio_lisays_paluuarvo(self):
          kopioi_ja_lisaa = load(exercise, function1, 'fi')
          s = [
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
          vas = kopioi_ja_lisaa(s, 0, 1, 3)
          self.assertFalse(vas == None, f'Funktion kopioi_ja_lisaa pitäisi palauttaa kaksiulotteinen kokonaislukutaulukko. Funktio ei palauta nyt mitään')
          self.assertTrue(type(vas) is list, f'Funktion kopioi_ja_lisaa pitäisi palauttaa kaksiulotteinen kokonaislukutaulukko. Funktion paluuarvo on nyt \n{vas}')
          try:   
            self.assertTrue(type(vas[0]) is list, f'Funktion kopioi_ja_lisaa pitäisi palauttaa kaksiulotteinen kokonaislukutaulukko. Funktion paluuarvo on nyt \n{vas}')
            self.assertTrue(type(vas[0][0]) is int, f'Funktion kopioi_ja_lisaa pitäisi palauttaa kaksiulotteinen kokonaislukutaulukko. Funktion paluuarvo on nyt \n{vas}')
          except:
            self.assertTrue(False, f'Funktion kopioi_ja_lisaa pitäisi palauttaa kaksiulotteinen kokonaislukutaulukko. Funktion paluuarvo on nyt \n{vas}')
          self.assertTrue(len(vas) == len(s), f'Kutsuttaessa \n{p(s)}\kopioi_ja_lisaa(s, 0, 1, 3) paluuarvon pitäisi olla samankokoinen matriisi kun parametrin, nyt se oli\n{vas}')
          self.assertTrue(len(vas[0]) == len(s[0]), f'Kutsuttaessa \n{p(s)}\kopioi_ja_lisaa(s, 0, 1, 3) paluuarvon pitäisi olla samankokoinen matriisi kun parametrin, nyt se oli\n{vas}')

    def test_3_lisays_toimii_1(self):  
        kopioi_ja_lisaa = load(exercise, function1, 'fi')
        for r, s, luku in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]

          try:
            vast = kopioi_ja_lisaa(sudoku, r, s, luku)
          except:
             self.assertTrue(False, f"Varmista että seruraava funktiokutsu toimii\n{p(sudoku)}")

          for rnro in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            if rnro == r:
              o[s] = luku
            self.assertEqual(vast[rnro], o, f"Funktiokutsu\n{p(sudoku)}\nvast = kopioi_ja_lisaa(s, {r}, {s}, {luku})\nei saa muuttaa parametrina olevaa matriisia sudoku, sen rivi {rnro} pitäisi olla:\n{o}:\nse kuitenkin on:\n{vast[rnro]}")
              
          for rnro in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            self.assertEqual(sudoku[rnro], o, f"Funktiokutsu\n{p(sudoku)}\nvast = kopioi_ja_lisaa(s, {r}, {s}, {luku})\npalauttaman matriisin vast rivin {rnro} pitäisi edelleen olla:\n{o}:\nse kuitenkin muuttunut muotoon:\n{vast[rnro]}")
                      
    def test_4_lisays_toimii_2(self):  
        kopioi_ja_lisaa = load(exercise, function1, 'fi')
        for r, s, luku in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]
          original = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          ]

          for rr in range(9):
            rivi = [1,2,3,4,5,6,7,8,9]
            shuffle(rivi)

            for ss in range(9):
              if randint(1,10)>5 and not (rr!=r and ss!=s):
                luku = rivi[ss]
                sudoku[r][s] = luku
                original[r][s] = luku

          try:
            vast = kopioi_ja_lisaa(sudoku, r, s, luku)
          except:
             self.assertTrue(False, f"Varmista että seruraava funktiokutsu toimii\n{p(sudoku)}")

          for rnro in range(9):
            o = sudoku[rnro]
            if rnro == r:
              o[s] = luku
            self.assertEqual(vast[rnro], o, f"Funktiokutsu\n{p(sudoku)}\nvast = kopioi_ja_lisaa(s, {r}, {s}, {luku})\nei saa muuttaa parametrina olevaa matriisia sudoku, sen rivi {rnro} pitäisi olla:\n{o}:\nse kuitenkin on:\n{vast[rnro]}")
              
          for rnro in range(9):
            o = original[rnro]
            self.assertEqual(sudoku[rnro], o, f"Funktiokutsu\n{p(sudoku)}\nvast = kopioi_ja_lisaa(s, {r}, {s}, {luku})\npalauttaman matriisin vast rivin {rnro} pitäisi edelleen olla:\n{o}:\nse kuitenkin muuttunut muotoon:\n{vast[rnro]}")

if __name__ == '__main__':
    unittest.main()
