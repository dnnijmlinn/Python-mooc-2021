import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from string import ascii_lowercase

exercise = 'src.salasanan_arpoja'
function = "luo_salasana"

def caseok(s: str):
    return len([x for x in s if x not in ascii_lowercase]) == 0



@points('7.salasanan_arpoja_1')
class SalasananArpoja1Test(unittest.TestCase):
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
            from src.salasanan_arpoja import luo_salasana
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä luo_salasana(pituus: int)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.salasanan_arpoja import luo_salasana
            val = luo_salasana(2)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == str, 
                f"Funktion lottonumerot pitäisi palauttaa arvo, joka on tyyppiä str, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametrilla (2)")
            
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvolla (2)")

    def test3_import_lause_mukana(self):
        with open("src/salasanan_arpoja.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Ohjelmassasi ei tuoda random-kirjastoa käyttöön import-lauseella.")
    

    def test4_testaa_arvoilla(self):
        test_cases = [2, 4, 5, 8, 11, 13, 20]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                luo_salasana = load(exercise, function, 'fi')

                val1 = luo_salasana(test_case)
                val2 = luo_salasana(test_case)

                self.assertTrue(len(val1) == test_case, f"Salasanan pituus {len(val1)}, vaikka sen pitäisi olla {test_case} kun parametri on {test_case}: {val1}")
                self.assertTrue(caseok(val1), f"Salasanassa on muita merkkejä kuin pieniä kirjaimia: \n{val1} \nkun parametri oli {test_case}")
                self.assertTrue(caseok(val2), f"Salasanassa on muita merkkejä kuin pieniä kirjaimia: \n{val2} \nkun parametri oli {test_case}") 
                self.assertNotEqual(val1, val2, f"Funktio palauttaa saman salasanan joka kutsulla: \n{val1} \nkun parametri on {test_case}")
                
    
    
    
              
if __name__ == '__main__':
    unittest.main()
