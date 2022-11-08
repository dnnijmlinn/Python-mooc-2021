import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.satunnaiset_sanat'
function = "sanat"

def unique(lst: list):
    return len(set(lst)) == len(lst)

def equal(lst1: list, lst2: list):
    return sorted(lst1) == sorted(lst2)

def correct_items(lst: list, s: str):
    return len([x for x in lst if not x.startswith(s)]) == 0

@points('7.satunnaiset_sanat')
class SatunnaisetSanatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[open('test/sanat.txt'), open('test/sanat.txt'),open('test/sanat.txt')]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test1_funktio_olemassa(self):
        with patch('builtins.open', side_effect=[open('test/sanat.txt'), open('test/sanat.txt'),open('test/sanat.txt')]):
            try:
                from src.satunnaiset_sanat import sanat
            except:
                self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä sanat(maara: int, alku: str)")

    def test2_palautusarvon_tyyppi(self):
        with patch('builtins.open', side_effect=[open('test/sanat.txt'), open('test/sanat.txt'),open('test/sanat.txt')]):
            try:
                from src.satunnaiset_sanat import sanat
                val = sanat(2, "car")
                taip = str(type(val)).replace("<class '","").replace("'>","")
                self.assertTrue(type(val) == list, 
                    f"Funktion sanat pitäisi palauttaa arvo, joka on tyyppiä list, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametreilla (2, 'car')")
                
            except Exception as ioe:
                self.assertTrue(False, f'Varmista että funktiokutsu sanat(2, "car") onnistuu')

    def test3_import_lause_mukana(self):
        with open("src/satunnaiset_sanat.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Ohjelmassasi ei tuoda random-kirjastoa käyttöön import-lauseella.")
    
    def test4_testaa_loytyvat(self):
        test_cases = [(5, "car"), (4, "abs"), (7, "of"), (10, "des")]
        for test_case in test_cases:
            with patch('builtins.open', side_effect=[open('test/sanat.txt'), open('test/sanat.txt'),open('test/sanat.txt'), open('test/sanat.txt')]):
                reload_module(self.module)
                sanat = load(exercise, function, 'fi')

                val1 = sanat(test_case[0], test_case[1])
                val2 = sanat(test_case[0], test_case[1])

                self.assertTrue(len(val1) == test_case[0], f"Listassa on {len(val1)} alkiota, vaikka siinä pitäisi olla {test_case[0]} alkiota kun parametrit ovat {test_case}: {val1}")
                self.assertTrue(unique(val1), f"Listan kaikki arvot eivät ole uniikkeja: {val1} kun parametrit olivat {test_case}")
                self.assertTrue(unique(val2), f"Listan kaikki arvot eivät ole uniikkeja: {val2} kun parametrit olivat {test_case}")
                self.assertFalse(equal(val1, val2), f"Funktio palauttaa samat arvot joka kutsulla: {val1} kun parametrit ovat {test_case}")
                self.assertTrue(correct_items(val1, test_case[1]), 
                    f"Listan kaikki alkiot eivät ala merkkijnolla {test_case[1]}: \n{val1}, \nkun parametrit ovat {test_case} ")

    def test5_testaa_ei_loytyvat(self):
        test_cases = [(500, "car"), (45, "absol"), (10, "superd")]
        for test_case in test_cases:
            with patch('builtins.open', side_effect=[open('test/sanat.txt'), open('test/sanat.txt'), open('test/sanat.txt'), open('test/sanat.txt')]):
                reload_module(self.module)
                sanat = load(exercise, function, 'fi')

                try:
                    val1 = sanat(test_case[0], test_case[1])
                    self.assertTrue(False, 
                        f"Funktion pitäisi tuottaa virhe ValueError parametreilla {test_case}, koska sanoja ei ole tiedostossa tarpeeksi. Nyt funktio palauttaa {val1}.")
                except ValueError:
                    pass  
              
if __name__ == '__main__':
    unittest.main()
