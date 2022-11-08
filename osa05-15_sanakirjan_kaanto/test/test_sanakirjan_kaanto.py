import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.sanakirjan_kaanto'
function = 'kaanna'

def get_correct(test_case: dict) -> dict:
    return {test_case[x] : x  for x in test_case}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.sanakirjan_kaanto')
class SanakirjaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
             from src.sanakirjan_kaanto import kaanna
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä kaanna(sanakirja: dict)')
        try:
            kaanna = load(exercise, function, 'fi')
            kaanna({1:10,2:20})
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nkaanna({1: 10, 2: 20})')


    def test_2_paluuarvon_tyyppi(self):
        kaanna = load(exercise, function, 'fi')
        test_case = {1:100} 
        try:
           val = kaanna({1:10})
        except:
            self.assertTrue(False, f'Varmista, että seuraava funktiokutsu onnistuu kaanna({test_case})')
   
        self.assertTrue(val == None, f"Funktion {function} ei tule palauttaa mitään, nyt se palauttaa arvon tyyppiä {type(val)}.")
    
    def test_3_kaanna(self):
        test_cases = ({1:10,2:20,3:30}, {-1:1, -2:2, -3:3, -5:5, -10:10}, {x : x * 100 for x in range(1,10)}, {x: x-1 for x in range(10,90,10)})
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kaanna = load(exercise, function, 'fi')
                
                test_case2 = test_case.copy()
                correct = get_correct(test_case)
                try:
                    kaanna(test_case)
                except:
                    self.assertTrue(False, f'Varmista, että seuraava funktiokutsu onnistuu kaanna({test_case})')
   
                self.assertEqual(len(correct), len(test_case), f"Palautetussa sanakirjassa pitäisi olla {len(correct)} alkiota, mutta siinä on {len(test_case)} alkiota: \n{test_case}\nkutsuttaessa kaanna({test_case2})")
                self.assertEqual(test_case, correct, f"Tulos \n{test_case}\nei vastaa mallivastausta \n{correct}\nkutsuttaessa kaanna({test_case2})")   
             
if __name__ == '__main__':
    unittest.main()
