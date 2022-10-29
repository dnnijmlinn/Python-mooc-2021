import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.risuaitaviiva'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace(" ", "") == str2.lower().replace(" ", "")

def get_correct(s : str) -> str:
    return int(s) * "#"
   

@points('3.risuaitaviiva')
class RisuaitaviivaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value="3"):
           cls.module = load_module(exercise, 'fi')


    def test_lyhyet(self):
        words = "5 3 2 6 1".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 1, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))

    def test_pitkat(self):
        words = "15 13 22 16 10".split(" ")
        for word in words:
            with patch('builtins.input', return_value = word):
                reload_module(self.module)
                output_all = get_stdout()
                output = [line.strip() for line in output_all.split("\n") if len(line) > 0]
                correct = get_correct(word)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä {} {} rivin sijasta {} riviä".
                    format(word, 1, len(output)))
                self.assertTrue(outputs_equal(output[0], correct), "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä {}".
                    format(output_all, correct, word))
    
    

    
    

if __name__ == '__main__':
    unittest.main()
