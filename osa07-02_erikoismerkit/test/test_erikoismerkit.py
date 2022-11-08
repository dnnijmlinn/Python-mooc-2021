import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.erikoismerkit'
function = "jaa_merkkeihin"



@points('7.erikoismerkit')
class ErikoismerkitTest(unittest.TestCase):
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
            from src.erikoismerkit import jaa_merkkeihin
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä jaa_merkkeihin(merkkijono: str)")

    def test2_palautusarvon_tyyppi(self):
        from src.erikoismerkit import jaa_merkkeihin
        val = jaa_merkkeihin("1.ö")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == tuple, f"Funktion jaa_merkkeihin pitäisi palauttaa arvo, joka on tyyppiä tuple, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametrilla '1.ö'")
        self.assertTrue(len(val) == 3, f"Funktion jaa_merkkeihin pitäisi palauttaa tuple, jossa on kolme merkkijonoa. Nyt se palauttaa arvon {val} kun sitä kutsutaan parametrilla '1.ö'")

    def test3_import_lause_mukana(self):
        with open("src/erikoismerkit.py") as f:
            cont = f.read()
            self.assertTrue("ascii_letters" in cont,
                f"Ohjelmassasi ei käytetä string-moduulin funktiota ascii_letters.")
            self.assertTrue("punctuation" in cont,
                f"Ohjelmassasi ei käytetä string-moduulin funktiota punctuation.")

    def test4_testaa_arvoilla(self):
        test_cases = {"abc.!åäö": ("abc", ".!", "åäö"), 
                      "a. s, d: f; g* ": ("asdfg", ".,:;*", "     "), 
                      "Tämä on testi!!!! Vai onko? On.": ("TmontestiVaionkoOn", "!!!!?.", "ää     ")}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                hypotenuusa = load(exercise, function, 'fi')

                val = hypotenuusa(test_case)

                for i in range(3):
                    self.assertEqual(val[i], test_cases[test_case][i], f"Funktion palauttama merkkijono \n'{val[i]}' \nparametrin arvolla \n'{test_case}' \nei vastaa mallivastausta  \n'{test_cases[test_case][i]}'. Koko palautusarvo oli {val}.")
              
if __name__ == '__main__':
    unittest.main()
