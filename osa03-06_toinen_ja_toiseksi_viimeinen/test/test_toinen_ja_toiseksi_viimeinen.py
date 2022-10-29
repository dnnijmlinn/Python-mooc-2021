import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.toinen_ja_toiseksi_viimeinen'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

@points('3.toinen_ja_toiseksi_viimeinen')
class ToinenJaToiseksiViimeinenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="sana"):
           cls.module = load_module(exercise, 'fi')

    def test_samat(self):
        words = "kanat tom-tom lottokeot abccba pip hullut xyzzzzyz".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {word}")
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = "Toinen ja toiseksi viimeinen kirjain on " + word[1]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} yhden rivin sijasta {} riviä".format(word, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output[0], correct, word))

    def test_eri(self):
        words = "kakku xyxy testi abbab töllit pidempitesti".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {word}")
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = "Toinen ja toiseksi viimeinen kirjain eroavat"
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} yhden rivin sijasta {} riviä".format(word, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output[0], correct, word))
    

if __name__ == '__main__':
    unittest.main()
