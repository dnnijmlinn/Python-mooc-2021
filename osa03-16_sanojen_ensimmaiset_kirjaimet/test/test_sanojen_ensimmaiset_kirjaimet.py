import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.sanojen_ensimmaiset_kirjaimet'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(s : str) -> str:
    return "\n".join([x[0] for x in s.split()])

@points('3.sanojen_ensimmaiset_kirjaimet')
class SanojenEnsimmaisetKirjaimetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = "x"):
           cls.module = load_module(exercise, 'fi')

    def test_lyhyet_lauseet(self):
        words = ["Heipparallaa", "Terve kaikille", "Moi vaan kaikille", "Simsalabim, sanoi taikuri", 
            "Mitäpä tässä hötkyilemään", "Vielä yksi testilause tässä"]
        for testcase in words:
            with patch('builtins.input', return_value = testcase):
                try:
                    reload_module(self.module)
                except:
                     self.assertFalse(True, f"varmista että ohjelmasti toimii syötteellä\n{testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(testcase)
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + testcase) 

                self.assertTrue(len(output) == len_correct, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, len_correct, len(output), output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct, testcase))

    def test_pidemmat_lauseet(self):
        words = ["Mitäpä tässä turhia jaarittelemaan, vaan jaarittelenpa tovin sittenkin.", 
            "Tässäpä vähän pidempi testilause: nähdään samantien miten hyvin ohjelma toimii",
            "Otetaanpa vielä yksi testi tähän loppuun: tässä lauseessa onkin aika paljon sanoja."]
        for testcase in words:
            with patch('builtins.input', return_value = testcase):
                try:
                    reload_module(self.module)
                except:
                     self.assertFalse(True, f"varmista että ohjelmasti toimii syötteellä\n{testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(testcase)
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + testcase) 

                self.assertTrue(len(output) == len_correct, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, len_correct, len(output), output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct, testcase))

if __name__ == '__main__':
    unittest.main()
