import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.tasaus_oikeaan'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return (20 - len(s)) * "*" + s
   

@points('3.tasaus_oikeaan')
class TasausOikeaanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="3"):
           cls.module = load_module(exercise, 'fi')


    def test_lyhyet_sanat(self):
        words = "testi heippa simsalabim zorro viuh!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 1, len(output)))
                self.assertTrue(output_all.count("*") == 20 - len(word), "Ohjelmasi tulostaa {} tähteä oikean määrän {} sijasta syötteellä {}: \n{}".
                    format(output_all.count("*"), (20 - len(word)), word, output_all))
                self.assertTrue(len(output_all) == 20, "Tulosteesi pituus on {} merkkiä 20 sijasta. Tulostit\n{}\nOdotettin\n{}".format(len(output_all), output_all, correct))
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{}\nsyötteellä {}".
                    format(output_all, correct, word))

    def test_pitkat_sanat(self):
        words = "keinutuolikauppa tosipitkayhdistelma abcdefghijkl melkein20merkkia!!!".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = output_all.split("\n")
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 1, len(output)))
                self.assertTrue(output_all.count("*") == 20 - len(word), "Ohjelmasi tulostaa {} tähteä oikean määrän {} sijasta syötteellä {}: \n{}".
                    format(output_all.count("*"), (20 - len(word)), word, output_all))
                self.assertTrue(len(output_all) == 20, "Tulosteesi pituus on {} merkkiä 20 sijasta. Tulostit\n{}\nOdotettin\n{}".format(len(output_all), output_all, correct))
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))

if __name__ == '__main_':
    unittest.main()
