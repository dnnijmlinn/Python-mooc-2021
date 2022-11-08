import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kurssin_tulokset_osa3'

def f(d):
    return '\n'.join(d)

def w(x):
    return [f"test/{i}" for i in x]

@points('6.kurssin_tulokset_osa3')
class KurssinTuloksetOsa3Test(unittest.TestCase):
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
        
            exp = """nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3"""
            expRows = exp.split('\n')

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 
            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}\n{mssage}") 
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            self.assertEqual(output[0], expRows[0], f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nEnsimmäisen tulostettavan rivin pitäisi olla\n{expRows[0]}\nSe on nyt\n{output[0]}\nOhjelman koko tulostus on:\n{output_all}")
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
        
            exp = """nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 25        6         11        17        1
jaana javanainen              27        6         10        16        1
liisa virtanen                35        8         6         14        0
donald frump                  0         0         15        15        1
john doe                      28        7         16        23        3
angela tarkel                 32        8         13        21        3
karkki eila                   30        7         7         14        0
alan turing                   28        7         19        26        4
ada lovelace                  27        6         27        33        5"""
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
        
            exp = """nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 25        6         9         15        1
jaana javanainen              30        7         11        18        2
liisa virtanen                34        8         14        22        3
donald frump                  40        10        0         10        0
john doe                      36        9         10        19        2
angela tarkel                 16        4         13        17        1
karkki eila                   26        6         10        16        1
alan turing                   24        6         17        23        3
ada lovelace                  26        6         24        30        5"""
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
        
            exp = """nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka pelokas                 25        6         6         12        0
mirja virtanen                30        7         8         15        1
jane doe                      33        8         14        22        3
donald frump                  35        8         16        24        4
john doe                      36        9         20        29        5
kalle paakkola                16        4         9         13        0
eila kaisla                   29        7         19        26        4
antti tuuri                   18        4         8         12        0
leena lempinen                26        6         10        16        1
eero honkela                  21        5         11        16        1"""
            expRows = exp.split('\n')

            self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä\n{f(words)}")
            output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
            self.assertEqual(len(expRows), len(output), f"Ohjelmasi tulostaa {len(expRows)} rivin sijaan {len(output)} riviä:\n{output_all}\nsyötteellä:\n{f(words)}\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}")
            for i in range(len(expRows)):
                line = output[i]
                self.assertTrue(line.strip() in exp, f"Ohjelmasi toimii väärin syötteellä\n{f(words)}\nrivi {line} ei ole odotetun kaltainen\nTulostuksen pitäisi sisältää seuraavat rivit:\n{exp}\nOhjelman koko tulostus on:\n{output_all}")
              
if __name__ == '__main__':
    unittest.main()
