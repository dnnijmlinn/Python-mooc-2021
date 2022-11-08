import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kurssin_tulokset_osa1'

def f(d):
    return '\n'.join(d)

def w(x):
    return [f"test/{i}" for i in x]

import os
from shutil import copyfile


@points('6.kurssin_tulokset_osa1')
class KurssinTuloksetOsa1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['test/opiskelijat1.csv', 'test/tehtavat1.csv', 'kolmas']):
           cls.module = load_module(exercise, 'fi')

    def test_1_toimii_tiedostoilla_1(self):
        words = ['opiskelijat1.csv', 'tehtavat1.csv']
        with patch('builtins.input', side_effect = w(words) + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 21
jaana javanainen 27
liisa virtanen 35"""
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
        words = ['opiskelijat2.csv', 'tehtavat2.csv']
        with patch('builtins.input', side_effect =w(words)  + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 25
jaana javanainen 27
liisa virtanen 35
donald frump 0
john doe 28
angela tarkel 32
karkki eila 30
alan turing 28
ada lovelace 17"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")


    def test_3_toimii_tiedostoilla_3(self):
        words = ['opiskelijat3.csv', 'tehtavat3.csv']
        with patch('builtins.input', side_effect =w(words)  + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka peloton 25
jaana javanainen 30
liisa virtanen 34
donald frump 40
john doe 36
angela tarkel 16
karkki eila 26
alan turing 24
ada lovelace 26"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")

    def test_4_toimii_tiedostoilla_4(self):
        words = ['opiskelijat4.csv', 'tehtavat4.csv']
        with patch('builtins.input', side_effect =w(words)  + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """pekka pelokas 25
mirja virtanen 30
jane doe 33
donald frump 35
john doe 36
kalle paakkola 16
eila kaisla 29
antti tuuri 18
leena lempinen 26
eero honkela 21"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")

if __name__ == '__main__':
    unittest.main()
