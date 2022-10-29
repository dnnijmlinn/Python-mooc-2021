import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.merkkien_maara'

@points('2.merkkien_maara')
class MerkkienMaaraTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_pitkat_sanat(self):
        words = "auto helikopteri lentokone mopedi fillari".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  +word)  
                self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa syötteellä {} kahden rivin sijasta {} riviä".format(word, len(output)))
                self.assertTrue(output[0].find(str(len(word))) > -1, "Ohjelmasi tulosteesta\n{}\nei löydy oikeaa pituutta {} syötteellä {}".format(output[0], len(word), word))
                self.assertEqual(sanitize(output[1]), "Kiitos!", "Ohjelmasi ei tulosta lopuksi Kiitos! syötteellä " +word)  

    def test_yksittainen_merkki(self):
        words = "a X z".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  +word)   
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} yhden rivin sijasta riviä sijasta {} riviä".format(word, len(output)))
                self.assertEqual(sanitize(output[0]), "Kiitos!", "Ohjelmasi ei tulosta lopuksi Kiitos! syötteellä " +word)  
   
if __name__ == '__main__':
    unittest.main()
