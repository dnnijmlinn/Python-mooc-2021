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

exercise = 'src.kuka_huijasi'
function = "huijarit"

                
def format(f):
    return ", ".join(f)

def file_exists(f: str):
    try:
        open(f)
        return True
    except:
        return False

def get_missing(result: list, correct: list):
    return [x for x in correct if x not in result]

def get_extra(result: list, correct: list):
    return [x for x in result if x not in correct]

filename1 = "tentin_aloitus.csv"
filename2 = "palautus.csv"


@points('7.kuka_huijasi')
class KukaHuijasiTest(unittest.TestCase):
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
            from src.kuka_huijasi import huijarit
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä huijarit()')
 
    def test2_palautusarvon_tyyppi(self):
        huijarit = load(exercise, function, 'fi')
        try:
            result = huijarit()
        except:
            self.assertTrue(False, 'Funktiota huijarit suorittaessa tapahtui virhe, tarkasta ohjelman toimivuus')
        
        taip = str(type(result)).replace("<class '","").replace("'>","")
        self.assertTrue(type(result) == list, f"Funktion huijarit tulisi palauttaa lista, nyt se palauttaa arvon {result} joka on tyyppiä {taip}")

    def test3_listan_sisalto(self):
        correct = ['matti', 'antti', 'henrik', 'arto', 'esko', 'kjell', 'jyrki', 'teemu', 'tiina', 'virpi', 'liisa', 'kotivalo', 'justiina', 'luukas', 'johannes']
        huijarit = load(exercise, function, 'fi')
        try:
            result = huijarit()
        except:
            self.assertTrue(False, 'Funktiota huijarit suorittaessa tapahtui virhe, tarkasta ohjelman toimivuus')
        
        self.assertTrue(len(result) == len(correct), f"Palautettavassa listassa tulisi olla {len(correct)} alkiota, nyt siinä on {len(result)} alkiota: {result}")
        
        missing = get_missing(result, correct)
        extra = get_extra(result, correct)

        self.assertTrue(len(missing) == 0, f"Palautetulta listalta puuttuivat seuraavat nimet: {format(missing)}. Nyt lista oli {result}")
        self.assertTrue(len(extra) == 0, f"Palautetulla listalla oli seuraavat ylimääräiset nimet: {format(extra)}. Nyt lista oli {result}")
        self.assertEqual(sorted(correct), sorted(result), f"Listan sisältö {result} ei vastaa mallivastausta {correct}")
  
if __name__ == '__main__':
    unittest.main()
