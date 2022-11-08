import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.omakieli'
function = "suorita"

class OmaKieliTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('7.omakieli-osa1')
    def test1_funktio_olemassa(self):
        try:
            from src.omakieli import suorita
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä suorita")

    @points('7.omakieli-osa1')
    def test2_ei_silmukkaa(self):
        tests = []
        program1 = ["PRINT A","END"]
        result1 = [0]
        tests.append((program1,result1))
        program2 = ["MOV A 5","PRINT A"]
        result2 = [5]
        tests.append((program2,result2))
        program3 = ["MOV A 1","MOV B 1","ADD A B","ADD B A","ADD A B","ADD B A","PRINT A","PRINT B"]
        result3 = [5,8]
        tests.append((program3,result3))
        program4 = ["MOV A 2","MUL A A","MUL A A","MUL A A","MUL A A","PRINT A"]
        result4 = [65536]
        tests.append((program4,result4))
        program5 = ["MOV A 10","PRINT A","MOV B A","SUB B 8","PRINT B","SUB A B","PRINT A"]
        result5 = [10,2,8]
        tests.append((program5,result5))
        for test in tests:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                suorita = load(exercise, function, 'fi')
                try:
                    result = suorita(test[0])
                except:
                    self.assertFalse(True, "Ohjelma "+str(test[0])+" aiheuttaa virheen")
                self.assertEqual(result, test[1], "Ohjelma "+str(test[0])+" tuottaa tuloksen "+str(result)+", oikea tulos olisi "+str(test[1]))

    @points('7.omakieli-osa2')
    def test3_kaikki_komennot(self):
        tests = []
        program1 = ["PRINT A","END"]
        result1 = [0]
        tests.append((program1,result1))
        program2 = []
        result2 = []
        tests.append((program2,result2))
        program3 = ["MOV A 10","alku:","PRINT A","SUB A 1","IF A > 0 JUMP alku","END"]
        result3 = [10,9,8,7,6,5,4,3,2,1]
        tests.append((program3,result3))
        program4 = ["MOV A 1","MOV B 1","alku:","MUL A 2","ADD B 1","IF B != 101 JUMP alku","PRINT A"]
        result4 = [1267650600228229401496703205376]
        tests.append((program4,result4))
        program5 = ["MOV A 1","MOV B 999","alku:","ADD A 1","SUB B 1","ADD C 1","IF A == B JUMP loppu","JUMP alku","loppu:","PRINT C"]
        result5 = [499]
        tests.append((program5,result5))
        program6 = ["MOV N 100","PRINT 2","MOV A 3","alku:","MOV B 2","MOV Z 0","testi:","MOV C B","uusi:","IF C == A JUMP virhe","IF C > A JUMP ohi","ADD C B","JUMP uusi","virhe:","MOV Z 1","JUMP ohi2","ohi:","ADD B 1","IF B < A JUMP testi","ohi2:","IF Z == 1 JUMP ohi3","PRINT A","ohi3:","ADD A 1","IF A <= N JUMP alku"]
        result6 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        tests.append((program6,result6))
        for test in tests:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                suorita = load(exercise, function, 'fi')
                try:
                    result = suorita(test[0])
                except:
                    self.assertFalse(True, "Ohjelma "+str(test[0])+" aiheuttaa virheen")
                self.assertEqual(result, test[1], "Ohjelma "+str(test[0])+" tuottaa tuloksen "+str(result)+", oikea tulos olisi "+str(test[1]))

if __name__ == '__main__':
    unittest.main()
