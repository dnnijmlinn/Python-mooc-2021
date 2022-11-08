import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.henkilot_talteen'
function = "tallenna_henkilo"
datafile = 'henkilot.csv'

def clear_file():
    with open(datafile, "w"):
        pass

def get_content():
    with open(datafile) as f:
        return [x.replace("\n","") for x in f.readlines() if len(x.strip()) > 0] 

def format(f):
    return "\n".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

@points('6.henkilot_talteen')
class HenkilotTalteenTest(unittest.TestCase):
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
            from src.henkilot_talteen import tallenna_henkilo
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä tallenna_henkilo(henkilo: tuple)")
        try:
            tallenna_henkilo(('Testi Testinen', 45, 160.0) )
        except:
            self.assertTrue(False, "Varmista, että seuraava funktiokutsu onnistuu tallenna_henkilo(('Testi Testinen', 45, 160.0))")


    def test_2_kirjoita_yksi_henkilo_1(self):
        test_case = ("Testi Testinen", 45, 160.0)
        clear_file()
        correct = ["Testi Testinen;45;160.0"]
        tallenna_henkilo = load(exercise, function, 'fi')
        try:
            tallenna_henkilo(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen parametreilla {test_case}: {ioe}")
        self.assertTrue(file_exists(datafile), f"Tiedostoa {datafile} ei löydy funktion suorituksen jälkeen!")

        data = get_content()

        self.assertTrue(len(data) == 1, 
            f"Tiedostosta {datafile} pitäisi löytyä 1 rivi kun funktiota on kutsuttu tyhjälle tiedostolle parametrilla {test_case} - nyt tiedostosta löytyi {len(data)} riviä.")

        self.assertEqual(data, correct, f"Tiedoston sisällön pitäisi olla \n{format(correct)} \nmutta se on \n{format(data)} \nkun funktiota kutsuttiin parametrilla {test_case}")
        
if False:
    def test_3_kirjoita_yksi_henkilo_2(self):
        test_case = ("Maija-Pirkko Virtanen-Lahtinen", 65, 155.5)
        clear_file()
        correct = ["Maija-Pirkko Virtanen-Lahtinen;65;155.5"]
        tallenna_henkilo = load(exercise, function, 'fi')
        try:
            tallenna_henkilo(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen parametreilla {test_case}: {ioe}")
        self.assertTrue(file_exists(datafile), f"Tiedostoa {datafile} ei löydy funktion suorituksen jälkeen!")

        data = get_content()

        self.assertTrue(len(data) == 1, 
            f"Tiedostosta {datafile} pitäisi löytyä 1 rivi kun funktiota on kutsuttu tyhjälle tiedostolle parametrilla {test_case} - nyt tiedostosta löytyi {len(data)} riviä.")

        self.assertEqual(data, correct, f"Tiedoston sisällön pitäisi olla \n{format(correct)} \nmutta se on \n{format(data)} \nkun funktiota kutsuttiin parametrilla {test_case}")

    def test_4_kirjoita_useampi_henkilo_2(self):
        test_cases = [("Maija Maijanen", 35, 175), ("Jarkko Jarkkonen", 19, 195.75), ("Aatu Aatula", 59, 167.0), ("Pikko Pirkkola", 84, 161.25)]

        clear_file()
        correct = []
        tallenna_henkilo = load(exercise, function, 'fi')
        for test_case in test_cases:
            try:
                tallenna_henkilo(test_case)
            except IOError as ioe:
                self.assertTrue(False, f"Funktio tuottaa tiedostovirheen parametreilla {test_case}: {ioe}")
            self.assertTrue(file_exists(datafile), f"Tiedostoa {datafile} ei löydy funktion suorituksen jälkeen!")

            data = get_content()
            correct.append((";".join(str(x) for x in test_case)))

            self.assertTrue(len(data) == len(correct), 
                f"Tiedostosta {datafile} pitäisi löytyä nyt {len(correct)} riviä kun funktiota on kutsuttu seuraavilla parametreilla:\n{format(correct)} \nNyt tiedostosta löytyi {len(data)} riviä: \n{format(data)})")

            self.assertEqual(data, correct, f"Tiedoston sisällön pitäisi olla \n{format(correct)} \nmutta se on \n{format(data)} \nkun funktiota on kutsuttu seuraavilla parametreilla:\n{format(correct)}")  
    
              
if __name__ == '__main__':
    unittest.main()
