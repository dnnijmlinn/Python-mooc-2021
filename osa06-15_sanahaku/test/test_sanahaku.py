import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.sanahaku'
function = "hae_sanat"

import os
from shutil import copyfile

def format(f):
    return "\n".join(f)

filename = "sanat.txt"

@points('6.sanahaku')
class SanahakuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            data_file = os.path.join('src', filename)
            copyfile(data_file, filename)
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        os.remove(filename)

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.sanahaku import hae_sanat
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä hae_sanat(hakusana: str)")
        
        try:
            val = hae_sanat("cat")
        except:        
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu hae_sanat("cat")')         
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == list, f'Funktion hae_sanat("cat") pitäisi palauttaa lista, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.')

    def test_2_haku_ei_erikoismerkkeja(self):
        test_case = ("cat")
        correct = ["cat"]
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")
        except: 
            self.assertTrue(False, f"Varmsta että funktion suorittaminen onnistuu hakusanalla {test_case}")

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")

    def test_3_haku_pisteet_1(self):
        test_case = ("ca.")
        correct = ['cab', 'cad', 'cal', 'cam', 'can', 'cap', 'car', 'cat', 'caw', 'cay']
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")

    def test_4_haku_pisteet_2(self):
        test_case = ("c.d.")
        correct = ['cads', 'cede', 'cmdg', 'coda', 'code', 'cods', 'cuds']
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")
        except: 
            self.assertTrue(False, f"Varmsta että funktion suorittaminen onnistuu hakusanalla {test_case}")   

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")
    
    def test_5_haku_pisteet_3(self):
        test_case = ("a...e")
        correct = ['abase', 'abate', 'abide', 'abode', 'above', 'abuse', 'acute', 'adage', 'addle', 'adobe', 'adore', 'adoze', 'aerie', 'afire', 
        'afore', 'agape', 'agate', 'agave', 'agaze', 'aggie', 'agile', 'aglee', 'agone', 'agree', 'aisle', 'alate', 'algae', 'alice', 'alike', 
        'aline', 'alive', 'alone', 'amaze', 'amble', 'amice', 'amide', 'amire', 'amole', 'amove', 'ample', 'amuse', 'andre', 'anele', 'angle', 
        'anile', 'anise', 'ankle', 'annie', 'anode', 'anole', 'antre', 'apace', 'apple', 'aquae', 'arete', 'argle', 
        'argue', 'arise', 'arose', 'aside', 'atone', 'aurae', 'autre', 'awake', 'aware', 'awoke', 'axone', 'azide', 'azine', 'azole', 'azote', 'azure']
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")
        except: 
            self.assertTrue(False, f"Varmsta että funktion suorittaminen onnistuu hakusanalla {test_case}")

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")

    def test_6_haku_asteriski1(self):
        test_case = ("reson*")
        correct = ['resonance', 'resonances', 'resonant', 'resonantly', 'resonants', 'resonate', 'resonated', 
            'resonates', 'resonating', 'resonation', 'resonations', 'resonator', 'resonators']
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")
        except: 
            self.assertTrue(False, f"Varmsta että funktion suorittaminen onnistuu hakusanalla {test_case}")     

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")

    def test_7_haku_asteriski2(self):
        test_case = ("*okes")
        correct = ['artichokes', 'backstrokes', 'blokes', 'breaststrokes', 'chokes', 'cokes', 'convokes', 
        'cowpokes', 'downstrokes', 'equivokes', 'evokes', 'heatstrokes', 'instrokes', 'invokes', 'jokes', 
        'keystrokes', 'pokes', 'provokes', 'reinvokes', 'revokes', 'sidestrokes', 'slowpokes', 
        'smokes', 'spokes', 'stokes', 'strokes', 'sunstrokes', 'tokes', 'unyokes', 'upstrokes', 'yokes']
        hae_sanat = load(exercise, function, 'fi')
        try:
            data = hae_sanat(test_case)
        except IOError as ioe:
            self.assertTrue(False, f"Funktio tuottaa tiedostovirheen hakusanalla {test_case}: {ioe}")
        except: 
            self.assertTrue(False, f"Varmsta että funktion suorittaminen onnistuu hakusanalla {test_case}")

        self.assertTrue(len(data) == len(correct), 
            f"Hakusanan {test_case} pitäisi palauttaa {len(correct)} riviä, nyt haku palautti {len(data)} riviä: \n{format(data)}")
        
        self.assertEqual(data, correct, f"Hakusanan {test_case} pitäisi palauttaa rivit \n{format(correct)} \nmutta funktio palautti rivit \n{format(data)}")

if __name__ == '__main__':
    unittest.main()
