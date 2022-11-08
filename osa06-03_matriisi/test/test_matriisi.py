import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.matriisi'

def get_correct() -> dict:
    pass

testdata = ["matriisi.txt"]

import os
from shutil import copyfile

@points('6.matriisi')
class MatriisiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen lukua ei pyydetty")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktiot_olemassa(self):
            try:
                from src.matriisi import rivisummat
            except:
                self.assertTrue(False, f'Koodistasi pitäisi löytyä funktiot nimillä rivisummat')  
            try:           
                rivisummat()
            except:
                self.assertTrue(False, f'Varmista että funktiokutsu rivisummat() onnistuu')

            try:
                from src.matriisi import maksimi
            except:
                self.assertTrue(False, f'Koodistasi pitäisi löytyä funktiot nimillä maksimi')
            try:
                maksimi()
            except:
                self.assertTrue(False, f'Varmista että metodikutsu maksimi() onnistuu')

            try:
                from src.matriisi import summa
            except:
                self.assertTrue(False, f'Koodistasi pitäisi löytyä funktiot nimillä summa')    
            try:
                summa()
            except:
                self.assertTrue(False, f'Varmista että metodikutsu summa() onnistuu')     

    def test_2_paluuarvojen_tyypit(self):
       
            funcs = "summa maksimi".split()
            for func in funcs:
                    fn = load(exercise, func, 'fi')
                    val = fn()
                    taip = str(type(val)).replace("<class '", '').replace("'>","")
                    self.assertTrue(type(val) == int, f"Funktion {func}() pitäisi palauttaa kokonaisluku, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
         
            fn = load(exercise, "rivisummat", 'fi')
            val = fn()
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == list, f"Funktion rivisummat() pitäisi palauttaa lista, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")

    def test_3_testaa_summa(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            summa = load(exercise, "summa", 'fi')

            val = summa()
            correct = 4542
            
            self.assertEqual(val, correct, f"Funktiokutsu summa() palauttaa arvon {val}, oikea vastaus on {correct}.")

    def test_4_testaa_maksimi(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            maksimi = load(exercise, "maksimi", 'fi')

            val = maksimi()
            correct = 965
            
            self.assertEqual(val, correct, f"Funktiokutsu maksimi() palauttaa arvon {val}, oikea vastaus on {correct}.")

    def test_5_testaa_rivisummat(self):
            reload_module(self.module)
            output_alussa = get_stdout()
            rivisummat = load(exercise, "rivisummat", 'fi')

            val = rivisummat()
            correct = [-1322, -41, 417, 916, 588, 1031, 880, 1748, -2421, -478, 3776, 346, 309, -881, -326]
            
            self.assertTrue(val == correct, f"Funktiokutsu rivisummat() palauttaa arvon\n{val}\noikea vastaus on\n{correct}")
                    
if __name__ == '__main__':
    unittest.main()
