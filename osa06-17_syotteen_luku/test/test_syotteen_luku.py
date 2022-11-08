import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.syotteen_luku'
function = 'lue'


@points('6.syotteen_luku')
class SyotteenLukuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=list(range(1000))):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
               
    def test_1_funktio_olemassa(self):
        try:
            from src.syotteen_luku import lue
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lue(pyynto: str, ala: int, yla: int)')

    def test_2_sopivat_luvut(self):
        with patch('builtins.input', side_effect=["7"]):
            lue = load(exercise, function, 'fi')
            try:
                tulos = lue("anna luku:", 2, 10)
            except:
                self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu lue("anna luku: ", 2, 10)')

            self.assertEqual(tulos, 7, "Funktio tulisi palauttaa arvo 7, kun käyttäjä antaa syötteen 7.")

    def test_3_liian_pienia1(self):
        with patch('builtins.input', side_effect=["4","6"]):
            lue = load(exercise, function, 'fi')
            tulos = lue("anna luku:", 5, 10)
            output = get_stdout()
            self.assertTrue("Syötteen on oltava kokonaisluku" in output, 
                "Funktion tulee tulostaa virheviesti 'Syötteen on oltava kokonaisluku väliltä 5...10', kun sitä kutsutaan parametreilla ('Anna luku', 5, 10) ja syöte on < 5.")
            self.assertEqual(tulos, 6, f"Funktio tulisi palauttaa arvo 6, kun käyttäjä antaa syötteen\n4\n6\nja funktiota kutsutaan parametreilla ('Anna luku', 5, 10). Nyt funktio palautti arvon {tulos}")

    def test_3_liian_pienia2(self):
        with patch('builtins.input', side_effect=["2","4","6"]):
            lue = load(exercise, function, 'fi')
            tulos = lue("anna luku:", 5, 10)
            output = get_stdout()
            self.assertTrue("Syötteen on oltava kokonaisluku" in output, 
                "Funktion tulee tulostaa virheviesti 'Syötteen on oltava kokonaisluku väliltä 5...10', kun sitä kutsutaan parametreilla ('Anna luku', 5, 10) ja syöte on < 5.")
            self.assertEqual(tulos, 6, f"Funktio tulisi palauttaa arvo 6, kun käyttäjä antaa syötteen\n2\n4\n6\nja funktiota kutsutaan parametreilla ('Anna luku', 5, 10). Nyt funktio palautti arvon {tulos}")

    def test_4_liian_suuria(self):
        with patch('builtins.input', side_effect=["10","20","30","40","4"]):
            lue = load(exercise, function, 'fi')
            tulos = lue("anna luku:", 1, 8)
            output = get_stdout()
            self.assertTrue("Syötteen on oltava kokonaisluku" in output, 
                "Funktion tulee tulostaa virheviesti 'Syötteen on oltava kokonaisluku väliltä 1...8', kun sitä kutsutaan parametreilla ('Anna luku', 1, 8) ja syöte on > 8.")
            self.assertEqual(tulos, 4, "Funktio tulisi palauttaa arvo 4, kun käyttäjä antaa syötteen \n10\n20\n30\n40\m4\nja funktiota  kutsutaan parametreilla ('Anna luku', 1, 8)")

    def test_5_ei_lukuja(self):
        with patch('builtins.input', side_effect=["yks","kaks","kolme","100"]):
            lue = load(exercise, function, 'fi')
            try:
                tulos = lue("anna luku:", 95, 105)
            except:
                self.assertTrue(False, "varmista että ohjelmasti suoritus onnistuu kun syöte on\nyks\nkaks\nkolme\n100")
            output = get_stdout()
            self.assertTrue("Syötteen on oltava kokonaisluku" in output, 
                "Funktion tulee tulostaa virheviesti 'Syötteen on oltava kokonaisluku väliltä 95...105', kun sitä kutsutaan parametreilla ('Anna luku', 95, 10) ja syöte koostuu kirjaimista.")
            self.assertEqual(tulos, 100, "Funktio tulisi palauttaa arvo 100, kun käyttäjä antaa syötteen 100 ja sitä kutsutaan parametreilla ('Anna luku', 95, 10)")
           
if __name__ == '__main__':
    unittest.main()
