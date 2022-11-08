import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
import os
from shutil import copyfile

exercise = 'src.kuka_huijasi_2'
function = "viralliset_pisteet"

                
def format(f):
    return ",".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def get_incorrect(result: dict, correct: dict):
    inc = {}
    for name in correct:
        if name not in result:
            inc[name] = correct[name]
        elif correct[name] != result[name]:
            inc[name] = correct[name]
    return inc


filename1 = "tentin_aloitus.csv"
filename2 = "palautus.csv"


@points('7.kuka_huijasi_2')
class KukaHuijasi2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            for filename in (filename1, filename2):
                data_file = os.path.join('src', filename)
                copyfile(data_file, filename)  
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
         os.remove(filename1)
         os.remove(filename2)

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test1_funktio_olemassa(self):
        try:
            from src.kuka_huijasi_2 import viralliset_pisteet
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä viralliset_pisteet()')
 
    def test2_palautusarvon_tyyppi(self):
        viralliset_pisteet = load(exercise, function, 'fi')
        try:
            result = viralliset_pisteet()
        except:
            self.assertTrue(False, 'Funktiota viralliset_pisteet suorittaessa tapahtui virhe, tarkasta ohjelman toimivuus')
        
        taip = str(type(result)).replace("<class '","").replace("'>","")
        self.assertTrue(type(result) == dict, f"Funktion viralliset_pisteet tulisi palauttaa sanakirja, nyt se palauttaa arvon {result} joka on tyyppiä {taip}")

    def test3_listan_sisalto(self):
        correct = {'matti': 43, 'erkki': 45, 'antti': 41, 'emilia': 42, 'henrik': 37, 'arto': 40, 'esko': 45, 'kjell': 47, 'jyrki': 41, 'teemu': 43, 'tiina': 36, 'jenna': 38, 'virpi': 39, 'kalle': 46, 'maija': 40, 'uolevi': 34, 'anna': 45, 'liisa': 42, 'kotivalo': 43, 'justiina': 44, 'matteus': 30, 'markus': 35, 'luukas': 40, 'johannes': 39}
        viralliset_pisteet = load(exercise, function, 'fi')
        try:
            result = viralliset_pisteet()
        except:
            self.assertTrue(False, 'Funktiota viralliset_pisteet suorittaessa tapahtui virhe, tarkasta ohjelman toimivuus')
        
        self.assertTrue(len(result) == len(correct), f"Palautettavassa sanakirjassa tulisi olla {len(correct)} alkiota, nyt siinä on {len(result)} alkiota: {result}")
        
        wrong = get_incorrect(result, correct)

        self.assertTrue(len(wrong) == 0, f"Seuraavat alkiot olivat väärin tai puuttuivat sanakirjasta: {wrong}. Nyt sanakirja oli {result} ja oikea vastaus {correct}")
        self.assertEqual(correct, result, f"Sanakirjan sisältö {format(result)} ei vastaa mallivastausta {format(correct)}")


        

  
if __name__ == '__main__':
    unittest.main()
