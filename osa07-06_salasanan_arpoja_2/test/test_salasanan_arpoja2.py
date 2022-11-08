import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from string import ascii_lowercase, digits

exercise = 'src.salasanan_arpoja2'
function = "luo_hyva_salasana"
punctuation = "!?=+-()#"

def chars_ok(s: str, g: str):
    return len([x for x in s if x not in g]) == 0

def contains(s: str, g: str):
    return any([x in s for x in g])
    



@points('7.salasanan_arpoja_2')
class SalasananArpoja2Test(unittest.TestCase):
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
            from src.salasanan_arpoja2 import luo_hyva_salasana
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkit: bool)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.salasanan_arpoja2 import luo_hyva_salasana
            val = luo_hyva_salasana(2,False,False)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == str, 
                f"Funktion lottonumerot pitäisi palauttaa arvo, joka on tyyppiä str, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametreilla (2, False, False)")
            
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvoilla (2, False, False)")

    def test3_import_lause_mukana(self):
        with open("src/salasanan_arpoja2.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "random" in cont, 
                f"Ohjelmassasi ei tuoda random-kirjastoa käyttöön import-lauseella.")
    

    def test4_testaa_pelkat_kirjaimet(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                luo_hyva_salasana = load(exercise, function, 'fi')

                val1 = luo_hyva_salasana(test_case, False, False)
                val2 = luo_hyva_salasana(test_case, False, False)

                self.assertTrue(len(val1) == test_case, f"Salasanan pituus on {len(val1)}, vaikka sen pitäisi olla {test_case} kun parametri on {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val1} \nkun parametrit olivat {test_case, False, False}")
                self.assertTrue(chars_ok(val2, ascii_lowercase), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val2} \nkun parametrit olivat {test_case, False, False}") 
                self.assertNotEqual(val1, val2, f"Funktio palauttaa saman salasanan joka kutsulla: \n{val1} \nkun parametri on {test_case}")

    def test5_testaa_kirjaimet_ja_numerot(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                luo_hyva_salasana = load(exercise, function, 'fi')

                val1 = luo_hyva_salasana(test_case, True, False)
                val2 = luo_hyva_salasana(test_case, True, False)

                self.assertTrue(len(val1) == test_case, f"Salasanan pituus {len(val1)}, vaikka sen pitäisi olla {test_case} kun parametri on {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + digits), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val1} \nkun parametrit olivat {test_case, True, False}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + digits), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val2} \nkun parametrit olivat {test_case, True, False}") 
                self.assertTrue(contains(val1, digits), f"Salasanassa ei ole yhtään merkkiä joukosta '{digits}': {val1} kun parametrit olivat {test_case, True, False} ")
                self.assertTrue(contains(val1, ascii_lowercase), f"Salasanassa ei ole yhtään merkkiä joukosta '{ascii_lowercase}': {val1} kun parametrit olivat {test_case, True, False} ") 
                self.assertNotEqual(val1, val2, f"Funktio palauttaa saman salasanan joka kutsulla: {val1} kun parametrit olivat {test_case, False, True}")

    def test6_testaa_kirjaimet_ja_erikois(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                luo_hyva_salasana = load(exercise, function, 'fi')

                val1 = luo_hyva_salasana(test_case, False, True)
                val2 = luo_hyva_salasana(test_case, False, True)

                self.assertTrue(len(val1) == test_case, f"Salasanan pituus {len(val1)}, vaikka sen pitäisi olla {test_case} kun parametri on {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + punctuation), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val1} \nkun parametrit olivat {test_case, False, True}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + punctuation), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val2} \nkun parametrit olivat {test_case, False, True}") 
                self.assertTrue(contains(val1, ascii_lowercase), f"Salasanassa ei ole yhtään merkkiä joukosta '{ascii_lowercase}': {val1} kun parametrit olivat {test_case, False, True} ") 
                self.assertTrue(contains(val1, punctuation), f"Salasanassa ei ole yhtään merkkiä joukosta '{punctuation}': {val1} kun parametrit olivat {test_case, False, True} ")
                self.assertNotEqual(val1, val2, f"Funktio palauttaa saman salasanan joka kutsulla: {val1} kun parametrit olivat {test_case, False, True}")

    def test7_testaa_kaikki(self):
        test_cases = [5,6,8,12,14,16]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                luo_hyva_salasana = load(exercise, function, 'fi')

                val1 = luo_hyva_salasana(test_case, True, True)
                val2 = luo_hyva_salasana(test_case, True, True)

                self.assertTrue(len(val1) == test_case, f"Salasanan pituus {len(val1)}, vaikka sen pitäisi olla {test_case} kun parametri on {test_case}: {val1}")
                self.assertTrue(chars_ok(val1, ascii_lowercase + punctuation + digits), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val1} \nkun parametrit olivat {test_case, True, True}")
                self.assertTrue(chars_ok(val2, ascii_lowercase + punctuation + digits), f"Salasanassa on muita merkkejä kuin sallittuja merkkejä: \n{val2} \nkun parametrit olivat {test_case, True, True}") 
                self.assertTrue(contains(val1, punctuation), f"Salasanassa ei ole yhtään merkkiä joukosta '{punctuation}': {val1} kun parametrit olivat {test_case, True, True} ")
                self.assertTrue(contains(val1, digits), f"Salasanassa ei ole yhtään merkkiä joukosta '{digits}': {val1} kun parametrit olivat {test_case, True, True} ") 
                self.assertTrue(contains(val1, ascii_lowercase), f"Salasanassa ei ole yhtään merkkiä joukosta '{ascii_lowercase}': {val1} kun parametrit olivat {test_case, True, True} ") 
                self.assertNotEqual(val1, val2, f"Funktio palauttaa saman salasanan joka kutsulla: {val1} kun parametrit olivat {test_case, True, True}")
                
                
    
    
    
              
if __name__ == '__main__':
    unittest.main()
