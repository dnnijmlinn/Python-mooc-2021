import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_lisays_ja_tulostus'
function1 = 'lisays'
function2 = 'tulosta'

def p(sudoku):
    j = 0
    m = 's = [\n'
    for rivi in sudoku:
        s = ', '.join([str(i) for i in rivi])
        m += f'  [ {s} ],\n'
        j += 1
    return m +']' 

@points('5.sudoku_lisays_ja_tulostus')
class SudokuLisaysTulostusTest(unittest.TestCase):
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
            from src.sudoku_lisays_ja_tulostus import tulosta
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä tulosta(sudoku: list)')
        try:
            from src.sudoku_lisays_ja_tulostus import tulosta
            tulosta = load(exercise, function2, 'fi')
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
            tulosta(s)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\ntulosta(s)')

    def test_2_tulostus_oikein(self):
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
      output_alussa = get_stdout()
      tulosta = load(exercise, function2, 'fi')
      tulosta(s)
      output_all = get_stdout().replace(output_alussa, '', 1)
      output = [l for l in output_all.split("\n") ]

      odotettu = [
       "9 _ _  _ 8 _  3 _ _",
        "2 _ _  2 5 _  7 _ _",
        "_ 2 _  3 _ _  _ _ 4",
        "",
        "2 9 4  _ _ _  _ _ _",
        "_ _ _  7 3 _  5 6 _",
        "7 _ 5  _ 6 _  4 _ _",
        "",
        "_ _ 7  8 _ 3  9 _ _",
        "_ _ 1  _ _ _  _ _ 3",
        "3 _ _  _ _ _  _ _ 2"
      ]

      for i in range(len(odotettu)):
        o = odotettu[i]
        v = output[i].replace('\n', '').rstrip()
        self.assertEqual(o, v, f'Funktiokutsussa\n{p(s)}\ntulosta(s)\ntulostuksen rivi {i+1} on väärin. Rivi oli:\n{v}\nsen pitäisi olla:\n{o}')

    def test_3_tulostus_oikein(self):
      s = [
          [2, 6, 7, 8, 3, 9, 5, 0, 4],
          [9, 0, 3, 5, 1, 0, 6, 0, 0],
          [0, 5, 1, 6, 0, 0, 8, 3, 9],
          [5, 1, 9, 0, 4, 6, 3, 2, 8],
          [8, 0, 2, 1, 0, 5, 7, 0, 6],
          [6, 7, 4, 3, 2, 0, 0, 0, 5],
          [0, 0, 0, 4, 5, 7, 2, 6, 3],
          [3, 2, 0, 0, 8, 0, 0, 5, 7],
          [7, 4, 5, 0, 0, 3, 9, 0, 1],
      ]  
      output_alussa = get_stdout()
      tulosta = load(exercise, function2, 'fi')
      tulosta(s)
      output_all = get_stdout().replace(output_alussa, '', 1)
      output = [l for l in output_all.split("\n") ]

      odotettu = [
        "2 6 7  8 3 9  5 _ 4",
        "9 _ 3  5 1 _  6 _ _",
        "_ 5 1  6 _ _  8 3 9",
        "",
        "5 1 9  _ 4 6  3 2 8",
        "8 _ 2  1 _ 5  7 _ 6",
        "6 7 4  3 2 _  _ _ 5",
        "",
        "_ _ _  4 5 7  2 6 3",
        "3 2 _  _ 8 _  _ 5 7",
        "7 4 5  _ _ 3  9 _ 1"
      ]

      for i in range(len(odotettu)):
        o = odotettu[i]
        v = output[i].replace('\n', '').rstrip()
        self.assertEqual(o, v, f'Funktiokutsussa\n{p(s)}\ntulosta(s)\ntulostuksen rivi {i+1} on väärin. Rivi oli:\n{v}\nsen pitäisi olla:\n{o}')

    def test_4_funktio_lisays_olemassa(self):
        try:
            from src.sudoku_lisays_ja_tulostus import lisays
        except:
            self.assertTrue(False, f'Koodistasi pitäisi löytyä funktio nimeltä lisays(sudoku: list, rivi: int, sarake: int, luku: int)')
        try:
            lisays = load(exercise, function1, 'fi')
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
            lisays(s, 0, 1, 3)
        except:
            self.assertTrue(False, f'Tarkista että funktiota voi kutsua seuraavasti\n{p(s)}\nlisays(s, 0, 1, 3)')

    def test_5_lisays_toimii(self):  
        lisays = load(exercise, function1, 'fi')
        for r, s, luku in [(1,1, 5), (0,0,1), (3, 4, 7), (2, 5, 8), (3, 5, 2)]:
          sudoku  = [
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
            lisays(sudoku, r, s, luku)
          except:
             self.assertTrue(False, f"Varmista että seuraava funktiokutsu toimii\n{p(sudoku)}\nlisays(s, {r}, {s}, {luku})")

          for rnro in range(9):
            o = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
            if rnro == r:
              o[s] = luku
            self.assertEqual(sudoku[rnro], o, f"Funktiokutsun\n{p(sudoku)}\nlisays(s, {r}, {s}, {luku})\nsuorituksen jälkeen rivin {rnro} (laskeminen alkaa 0:sta) pitäisi olla:\n{o}:\nse kuitenkin on:\n{sudoku[rnro]}")
              
if __name__ == '__main__':
    unittest.main()
