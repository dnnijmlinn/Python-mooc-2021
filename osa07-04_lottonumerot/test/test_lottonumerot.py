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

exercise = 'src.lottonumerot'
function = "lottonumerot"

def within_limits(lst: list, low: int, high: int):
    return len([x for x in lst if x < low or x > high]) == 0

def unique(lst: list):
    return len(set(lst)) == len(lst)

def is_sorted(lst: list):
    return sorted(lst) == lst



@points('7.lottonumerot')
class LottonumerotTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.lottonumerot import lottonumerot
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä lottonumerot(maara: int, alaraja: int, ylaraja: int)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.lottonumerot import lottonumerot
            val = lottonumerot(1, 1, 10)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, 
                f"Funktion lottonumerot pitäisi palauttaa arvo, joka on tyyppiä list, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametreilla (1,1,10)")
            
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvoilla (1,1,10)")

    def test3_import_lause_mukana(self):
        with open("src/lottonumerot.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Ohjelmassasi ei tuoda random-kirjastoa käyttöön import-lauseella.")
    

    def test4_testaa_arvoilla(self):
        f = Fraction
        test_cases = [(3,2,22), (5,10,100), (7,1,39)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                lottonumerot = load(exercise, function, 'fi')

                val1 = lottonumerot(test_case[0], test_case[1], test_case[2])
                val2 = lottonumerot(test_case[0], test_case[1], test_case[2])

                self.assertTrue(len(val1) == test_case[0], f"Listassa on {len(val1)} alkiota, vaikka siinä pitäisi olla {test_case[0]} alkiota kun parametrit ovat {test_case}: {val1}")
                self.assertTrue(unique(val1), f"Listan kaikki arvot eivät ole uniikkeja: \n{val1} \nkun parametrit olivat {test_case}")
                self.assertTrue(unique(val2), f"Listan kaikki arvot eivät ole uniikkeja: \n{val2} \nkun parametrit olivat {test_case}")
                self.assertNotEqual(val1, val2, f"Funktio palauttaa samat arvot joka kutsulla: \n{val1} \nkun parametrit ovat {test_case}")
                self.assertTrue(is_sorted(val1), f"Listan arvot eivät ole suuruusjärjestyksessä: \n{val1} \nkun parametrit ovat {test_case}")
                self.assertTrue(within_limits(val1, test_case[1], test_case[2]), 
                    f"Listassa on liian pieni tai liian suuri alkio kun parametrit olivat {test_case}: \n{val1} ")
                self.assertTrue(within_limits(val2, test_case[1], test_case[2]), 
                    f"Listassa on liian pieni tai liian suuri alkio kun parametrit olivat {test_case}: \n{val2} ")
    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
