import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.osajonot1'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return "\n".join([s[0 : i] for i in range(1, len(s) + 1)])
   

@points('3.osajonot1')
class Osajonot1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="auto"):
           cls.module = load_module(exercise, 'fi')
    def test_lyhyet(self):
        words = "auto pallo karkki kone moi se lakki nakki rakki".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {word}")
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == len(word), "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, len(word), len(output)))
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))
    
    def test_pitkat(self):
        words = "automaattinen superlatiivi ehdottomasti supercalifragilisticexpialidocus".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {word}")
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == len(word), "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, len(word), len(output)))
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))

if __name__ == '__main__':
    unittest.main()
