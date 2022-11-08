import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.elokuvarekisteri'
function = 'lisaa_elokuva'

def get_correct() -> dict:
    pass

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.elokuvarekisteri')
class ElokuvarekisteriTest(unittest.TestCase):
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
            from src.elokuvarekisteri import lisaa_elokuva
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int)')
        try:
            lisaa_elokuva = load(exercise, function, 'fi')
            lisaa_elokuva([], "", "", 1, 1)
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nlisaa_elokuva([], "", "", 1, 1)')


    def test_2_paluuarvon_tyyppi(self):
        lisaa_elokuva = load(exercise, function, 'fi')
        val = lisaa_elokuva([], "", "", 1, 1)
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(val == None, f"Funktion {function} ei pidä palauttaa mitään, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
    
    def test_3_testaa_yksi_elokuva(self):
        test_cases = (("Linnut", "Alfred Hitchcock", 1963, 119), ("Kummisetä", "Francis Ford Coppola", 1972, 175))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()

                lisaa_elokuva = load(exercise, function, 'fi')

                movielist = []
                
                correct = [{x : y for x,y in zip(("nimi","ohjaaja","vuosi","pituus"), test_case)}]
                lisaa_elokuva(movielist, test_case[0], test_case[1], test_case[2], test_case[3])
                

                self.assertEqual(len(correct), len(movielist), f"Lisäyksen jälkeen listalla pitäisi {len(correct)} alkiota, mutta siinä on {len(movielist)} alkiota: \n{movielist} kun parametrit ovat \n{test_case}")
                self.assertEqual(correct, movielist, f"Tulos \n{movielist}\nei vastaa mallivastausta \n{correct}\nkun parametrit ovat \n{test_case}")

    def test_3_testaa_useampi_elokuva(self):
        test_cases = (("Linnut", "Alfred Hitchcock", 1963, 119), 
                      ("Kummisetä", "Francis Ford Coppola", 1972, 175),
                      ("Tappajahai", "Steven Spielberg", 1975, 124), 
                      ("Star Wars", "George Lucas", 1977, 121))
        movielist = []
        correct = []
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                lisaa_elokuva = load(exercise, function, 'fi')

                correct.append({x : y for x,y in zip(("nimi","ohjaaja","vuosi","pituus"), test_case)})
                lisaa_elokuva(movielist, test_case[0], test_case[1], test_case[2], test_case[3])
                
                self.assertEqual(len(correct), len(movielist), f"Lisäyksen jälkeen listalla pitäisi {len(correct)} alkiota;\n{correct}, mutta siinä on {len(movielist)} alkiota: \n{movielist} kun parametrit ovat \n{test_case}")
                self.assertEqual(correct, movielist, f"Tulos \n{movielist}\nei vastaa mallivastausta \n{correct}\nkun parametrit ovat \n{test_case}")
              
if __name__ == '__main__':
    unittest.main()
