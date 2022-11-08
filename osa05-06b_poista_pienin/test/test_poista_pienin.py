import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.poista_pienin'
function = 'poista_pienin'


@points('5.poista_pienin')
class PoistaPieninTest(unittest.TestCase):
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
            from src.poista_pienin import poista_pienin
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä poista_pienin(luvut: list)' )
        try:
            from src.poista_pienin import poista_pienin
            poista_pienin([1, 2])
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\npoista_pienin([1,2])' )

    def test_2_paluuarvon_tyyppi(self):
        poista_pienin = load(exercise, function, 'fi')
        val = poista_pienin([1])
        self.assertTrue(val == None, f"Funktion {function} ei pidä palauttaa arvoa, nyt palautusarvon tyyppi on {type(val)}.")
    
    def test_3_listat(self):
        test_cases = ([1,2,3,5,6], [9,7,5,3], [10,13,15,9,11,12,14], [100,10], [1,2,3,-1,-2,-3], [-4,-5,-6,-3,-2])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                tuplaa_alkiot = load(exercise, function, 'fi')
                
                correct = [x for x in test_case if x != min(test_case)]
                test_case2 = test_case[:]

                try:
                    tuplaa_alkiot(test_case)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun syöte on \n{test_case2}")

                self.assertEqual(correct, test_case, f"Tulos \n{test_case} \nei vastaa mallivastausta \n{correct} \nkun syöte on \n{test_case2}")
            

              
if __name__ == '__main__':
    unittest.main()
