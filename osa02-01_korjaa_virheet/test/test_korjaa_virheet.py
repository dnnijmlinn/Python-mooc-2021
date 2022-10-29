import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.korjaa_virheet'


def p(a):
    return "\n".join(a)

@points('2.korjaa_virheet')
class KorjaaVirheetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_yli_sata_0(self):
        value = 101
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "varmista että pystyt suorittamaan ohjelman syötteellä {}".format(value))

    def test_alle_sata_0(self):
        value = 90
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "varmista että pystyt suorittamaan ohjelman syötteellä {}".format(value))

    def test_alle_sata_1(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Tulosteesta ei löydy oikeaa lukua {} syötteellä {}. Ohjelmasi tulosti\n{}".format(value, value, p(output)))
            malli = str(value) + " taitaa olla onnenlukuni!"
            self.assertEqual(sanitize(output[0]), malli, "Tulosteen 1. rivi ei vastaa mallivastausta {} syötteellä {}. Ohjelmasi tulosti\n{}".format(malli, value, p(output)))
            malli = "Hyvää päivänjatkoa!"
            self.assertEqual(sanitize(output[1]), malli, "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {} syötteellä {}. Ohjelmasi tulosti\n{}".format(malli, value, p(output)))
            
    def test_alle_sata_2(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Tulosteesta ei löydy oikeaa lukua {} syötteellä {}".format(value, value))
            malli = str(value) + " taitaa olla onnenlukuni!"
            self.assertEqual(sanitize(output[0]), malli, "Tulosteen 1. rivi ei vastaa mallivastausta {} syötteellä {}. Ohjelmasi tulosti\n{}".format(malli, value,p(output)))
            malli = "Hyvää päivänjatkoa!"
            self.assertEqual(sanitize(output[1]), malli, "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {} syötteellä {}. Ohjelmasi tulosti\n{}".format(malli, value, p(output)))
            
    def test_yli_sata_1(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Ohjelmasi tulostaa viiden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Tulosteesta ei löydy pienennettyä lukua {} syötteellä {}. Ohjelmasi tulosti\n{}".format(value - 100, value, p(output)))
            self.assertEqual(sanitize(output[0]), "Luku oli suurempi kuin sata", "Tulosteen 1. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[1]), "Nyt luvun arvo on pienentynyt sadalla", "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[3]), str(value - 100) + " taitaa olla onnenlukuni!", "Tulosteen 4. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[4]), "Hyvää päivänjatkoa!", "Tulosteen 5. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))

    def test_yli_sata_2(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Ohjelmasi tulostaa viiden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Tulosteesta ei löydy pienennettyä lukua {} syötteellä {}. Ohjelmasi tulosti\n{}".format(value - 100, value, p(output)))
            self.assertEqual(sanitize(output[0]), "Luku oli suurempi kuin sata", "Tulosteen 1. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[1]), "Nyt luvun arvo on pienentynyt sadalla", "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[3]), str(value - 100) + " taitaa olla onnenlukuni!", "Tulosteen 4. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
            self.assertEqual(sanitize(output[4]), "Hyvää päivänjatkoa!", "Tulosteen 5. rivi ei vastaa mallivastausta syötteellä {}. Ohjelmasi tulosti\n{}".format(value, p(output)))
    
if __name__ == '__main__':
    unittest.main()
