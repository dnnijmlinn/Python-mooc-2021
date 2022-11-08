import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.etsi_elokuvat'
function = 'etsi_elokuvat'

def get_correct(l: list, s: str) -> list:
    return [x for x in l if s.lower() in x["nimi"].lower()]

@points('5.etsi_elokuvat')
class EtsiElokuvatTest(unittest.TestCase):
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
            from src.etsi_elokuvat import etsi_elokuvat
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä etsi_elokuvat(rekisteri: list, hakusana: str)')
        try:
            etsi_elokuvat = load(exercise, function, 'fi')
            etsi_elokuvat([{"nimi":"aa", "ohjaaja":"", "vuosi":1, "pituus":1}], "a")
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\netsi_elokuvat([{"nimi":"aa", "ohjaaja":"", "vuosi":1, "pituus":1}], "a")')

    def test_2_paluuarvon_tyyppi(self):
        etsi_elokuvat = load(exercise, function, 'fi')
        val = etsi_elokuvat([{"nimi":"aa", "ohjaaja":"", "vuosi":1, "pituus":1}], "a")
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion {function} pitäisi palauttaa lista, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
    
    def test_3_elokuvat_1(self):
        test_cases = (("Linnut", "Alfred Hitchcock", 1963, 119), 
                      ("Kummisetä", "Francis Ford Coppola", 1972, 175),
                      ("Tappajahai", "Steven Spielberg", 1975, 124), 
                      ("Star Wars", "George Lucas", 1977, 121))
        movielist = []
        for tc in test_cases:
            movielist.append({x : y for x,y in zip(("nimi","ohjaaja","vuosi","pituus"), tc)})
        
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            output_alussa = get_stdout()
            etsi_elokuvat = load(exercise, function, 'fi')
            
            correct = get_correct(movielist, "ta")
            answer = etsi_elokuvat(movielist, "ta")
            
            self.assertEqual(len(correct), len(answer), f"Tuloksessa pitäisi olla {len(correct)} alkiota;\n{correct}, mutta siinä on {len(answer)} alkiota: \n{answer}\nkun rekisterissä on elokuvat \n{movielist} ja hakusana on 'ta'")
            self.assertEqual(correct, answer, f"Tulos \n{answer}\nei vastaa mallivastausta \n{correct}\nkun rekisterissä on elokuvat \n{movielist}\nja hakusana on 'ta'")
    
    def test_4_elokuvat_2(self):
        test_cases = (("Linnut 4", "James Hitchcock", 2003, 119), 
                      ("Kummisetä 4", "Antero Coppola", 2022, 83),
                      ("Tappajahai", "Steven Spielberg", 1975, 124), 
                      ("Star Wars", "George Lucas", 1977, 121), 
                      ("Lost in Translation 4", "Sofia Coppola", 2032, 120))
        movielist = []
        for tc in test_cases:
            movielist.append({x : y for x,y in zip(("nimi","ohjaaja","vuosi","pituus"), tc)})
        
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            output_alussa = get_stdout()
            etsi_elokuvat = load(exercise, function, 'fi')
            
            correct = get_correct(movielist, "4")
            answer = etsi_elokuvat(movielist, "4")
            
            self.assertEqual(len(correct), len(answer), f"Tuloksessa pitäisi olla {len(correct)} alkiota;\n{correct}, mutta siinä on {len(answer)} alkiota: \n{answer} kun rekisterissä on elokuvat \n{movielist} ja hakusana on '4'")
            self.assertEqual(correct, answer, f"Tulos \n{answer}\nei vastaa mallivastausta \n{correct}\nkun rekisterissä on elokuvat \n{movielist}\nja hakusana on '4'")
    
              
if __name__ == '__main__':
    unittest.main()
