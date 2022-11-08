import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kurssin_tulokset_osa2'

def f(d):
    return '\n'.join(d)
    
def w(x):
    return [f"test/{i}" for i in x]

@points('6.kurssin_tulokset_osa2')
class KurssinTuloksetOsa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['test/opiskelijat1.csv', 'test/tehtavat1.csv', 'test/koepisteet1.csv']):
           cls.module = load_module(exercise, 'fi')

    def test_1_toimii_tiedostoilla_1(self):
        words = ['opiskelijat1.csv', 'tehtavat1.csv', 'koepisteet1.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 0
jaana javanainen 1
liisa virtanen 3"""
            expRows = exp.split('\n')

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")

    def test_2_toimii_tiedostoilla_2(self):
        words = ['opiskelijat2.csv', 'tehtavat2.csv', 'koepisteet2.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 1
jaana javanainen 1
liisa virtanen 0
donald frump 1
john doe 3
angela tarkel 3
karkki eila 0
alan turing 4
ada lovelace 5"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")

    def test_3_toimii_tiedostoilla_3(self):
        words = ['opiskelijat3.csv', 'tehtavat3.csv', 'koepisteet3.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 1
jaana javanainen 2
liisa virtanen 3
donald frump 0
john doe 2
angela tarkel 1
karkki eila 1
alan turing 3
ada lovelace 5"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")

    def test_4_toimii_tiedostoilla_4(self):
        words = ['opiskelijat4.csv', 'tehtavat4.csv', 'koepisteet4.csv']
        with patch('builtins.input', side_effect =w(words) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka pelokas 0
mirja virtanen 1
jane doe 3
donald frump 4
john doe 5
kalle paakkola 0
eila kaisla 4
antti tuuri 0
leena lempinen 1
eero honkela 1"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")
              
if __name__ == '__main__':
    unittest.main()
