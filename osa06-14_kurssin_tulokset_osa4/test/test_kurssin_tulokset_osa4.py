import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kurssin_tulokset_osa4'

def f(d):
    return '\n'.join(d)

datafile1 = 'tulos.txt'
datafile2 = 'tulos.csv'

import os
from shutil import copyfile

testdata = ["koepisteet1.csv", "koepisteet2.csv", "koepisteet3.csv", "koepisteet4.csv",
"opiskelijat1.csv", "opiskelijat2.csv", "opiskelijat3.csv", "opiskelijat4.csv", "tehtavat1.csv", "tehtavat2.csv", "tehtavat3.csv", "tehtavat4.csv",
"kurssi1.txt", "kurssi2.txt", "kurssi3.txt", "kurssi4.txt"]

def get_correct() -> dict:
    pass

def clear_files():
    with open(datafile1, "w"), open(datafile2, "w"):
        pass

def get_content_1():
    with open(datafile1) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0]

def get_content_2():
    with open(datafile2) as f2:
        return [x.replace("\n","") for x in f2.readlines() if len(x.strip()) > 0]

@points('6.kurssin_tulokset_osa4')
class KurssinTuloksetOsa4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=['opiskelijat1.csv', 'tehtavat1.csv', 'koepisteet1.csv', 'kurssi1.txt']):
            for filename in testdata:
                data_file = os.path.join('src', filename)
                copyfile(data_file, filename)
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_1_toimii_tiedostoilla_1(self):
        words = ['opiskelijat1.csv', 'tehtavat1.csv', 'koepisteet1.csv', 'kurssi1.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """Ohjelmoinnin perusteet, 5 opintopistettä
========================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3"""
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
"""
            #\n{mssage}") 

            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.txt syötteellä\n{f(words)}\n{mssage}")  

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nRivi:\n{line}\nei ole odotetun kaltainen\nSen pitäisi olla:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\tiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(txt_file)}")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.csv syötteellä\n{f(words)}")    

        exp = """12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\ntiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(csv_file)}")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")


    def test_2_toimii_tiedostoilla_2(self):
        words = ['opiskelijat2.csv', 'tehtavat2.csv', 'koepisteet2.csv', 'kurssi2.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")
        
            exp = """Ohjelmoinnin jatkokurssi, 5 opintopistettä
==========================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 25        6         11        17        1         
jaana javanainen              27        6         10        16        1         
liisa virtanen                35        8         6         14        0         
donald frump                  0         0         15        15        1        
john doe                      28        7         16        23        3         
angela tarkel                 32        8         13        21        3         
karkki eila                   30        7         7         14        0         
alan turing                   28        7         19        26        4         
ada lovelace                  27        6         27        33        5   """
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.txt syötteellä\n{f(words)}")    

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nRivi:\n{line}\nei ole odotetun kaltainen\nSen pitäisi olla:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\tiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(txt_file)}")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.csv syötteellä\n{f(words)}")    

        exp = """12345678;pekka peloton;1
12345687;jaana javanainen;1
12345699;liisa virtanen;0
12345688;donald frump;1
12345698;john doe;3
12345700;angela tarkel;3
12345701;karkki eila;0
12345702;alan turing;4
12345704;ada lovelace;5"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\ntiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(csv_file)}")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")
    
    def test_3_toimii_tiedostoilla_3(self):
        words = ['opiskelijat3.csv', 'tehtavat3.csv', 'koepisteet3.csv', 'kurssi3.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")

            exp = """Tietorakenteet ja algoritmit, 10 opintopistettä
===============================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 25        6         9         15        1        
jaana javanainen              30        7         11        18        2        
liisa virtanen                34        8         14        22        3         
donald frump                  40        10        0         10        0         
john doe                      36        9         10        19        2         
angela tarkel                 16        4         13        17        1         
karkki eila                   26        6         10        16        1         
alan turing                   24        6         17        23        3         
ada lovelace                  26        6         24        30        5     """
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.txt syötteellä\n{f(words)}")    

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nRivi:\n{line}\nei ole odotetun kaltainen\nSen pitäisi olla:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\tiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(txt_file)}")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.csv syötteellä\n{f(words)}")    

        exp = """12345678;pekka peloton;1
12345687;jaana javanainen;2
12345699;liisa virtanen;3
12345688;donald frump;0
12345698;john doe;2
12345700;angela tarkel;1
12345701;karkki eila;1
12345702;alan turing;3
12345704;ada lovelace;5"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\ntiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(csv_file)}")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")
           
    def test_4_toimii_tiedostoilla_4(self):
        words = ['opiskelijat4.csv', 'tehtavat4.csv', 'koepisteet4.csv', 'kurssi4.txt']
        with patch('builtins.input', side_effect =words + [ AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
                output_all = get_stdout()
            except:
                self.assertTrue(False, f"Varmista, että ohjelmasi voidaan suorittaa syötteellä\n{f(words)}")

            exp = """Tietokoneen toiminnan perusteet, 2 opintopistettä
=================================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka pelokas                 25        6         6         12        0         
mirja virtanen                30        7         8         15        1       
jane doe                      33        8         14        22        3         
donald frump                  35        8         16        24        4        
john doe                      36        9         20        29        5         
kalle paakkola                16        4         9         13        0         
eila kaisla                   29        7         19        26        4         
antti tuuri                   18        4         8         12        0         
leena lempinen                26        6         10        16        1         
eero honkela                  21        5         11        16        1       """
            expRows = exp.split('\n')

        try:
            txt_file = get_content_1()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.txt syötteellä\n{f(words)}")    

        for i in range(3):
            line = txt_file[i]
            self.assertEqual(line.strip(), expRows[i], f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nRivi:\n{line}\nei ole odotetun kaltainen\nSen pitäisi olla:\n{exp}")

        self.assertEqual(len(txt_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\tiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(txt_file)}")
        for i in range(3, len(expRows)):
            line = txt_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.txt ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")

        try:
            csv_file = get_content_2()
        except:
            self.assertTrue(False, f"Ohjelmasi pitää luoda tiedosto tulos.csv syötteellä\n{f(words)}")    

        exp = """12345678;pekka pelokas;0
12345687;mirja virtanen;1
12345699;jane doe;3
12345688;donald frump;4
12345698;john doe;5
12345700;kalle paakkola;0
12345701;eila kaisla;4
12345702;antti tuuri;0
12345704;leena lempinen;1
12345709;eero honkela;1"""

        expRows = exp.split('\n')

        self.assertEqual(len(csv_file), len(expRows), f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\ntiedostossa pitäisi olla {len(expRows)} riviä, riveja on {len(csv_file)}")
        for i in range(0, len(expRows)):
            line = csv_file[i]
            self.assertTrue(line.strip() in exp, f"Ohjelmasi luoma tiedosto tulos.csv ei ole kunnossa syötteellä\n{f(words)}\nrivi\n{line}\nei ole odotetun kaltainen\nTiedoston pitäisi sisältää seuraavat rivit:\n{exp}")
           

if __name__ == '__main__':
    unittest.main()
