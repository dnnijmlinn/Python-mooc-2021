import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.osajonojen_haku'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(s : str, m: str) -> str:
    return "\n".join([s[i : i + 3] for i in range(0, len(s) - 2 ) if s[i] == m])
   

@points('3.osajonojen_haku')
class OsajonojenHakuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["apinatalo","a"]):
           cls.module = load_module(exercise, 'fi')

    def test_sanat_1(self):
        words = "apinatalo,a abcccabd,a töttöröö,t appilanpappilan,p simsalabim,s".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"Ohjelmasi ei suoritus ei onnistu syötteellä {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + word)  
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == cor_len, f"Ohjelmasi tulostaa syötteellä ({testcase}) {cor_len} rivin sijasta {len(output)} riviä. Oikea tuloste on\n{correct}")
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{output_all}\nei vastaa oikeaa tulostetta \n{correct} \nsyötteellä ({testcase})")

    def test_sanat_2(self):
        words = "puppureppu,p ohjelmointikieli,e appilanpappilanapupapinpapupata,a".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"Ohjelmasi ei suoritus ei onnistu syötteellä {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == cor_len, f"Ohjelmasi tulostaa syötteellä ({testcase}) {cor_len} rivin sijasta {len(output)} riviä. Oikea tuloste on\n{correct}")
                self.assertTrue(outputs_equal(output_all, correct), "Ohjelmasi tuloste\n{output_all}\nei vastaa oikeaa tulostetta \n{correct}\nsyötteellä ({testcase})")
    
    def test_sanat_3(self):
        words = "api,p python,o abcdefg,x".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                try:
                    reload_module(self.module)
                except:
                    self.assertTrue(False, f"Ohjelmasi ei suoritus ei onnistu syötteellä {testcase}")
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                word,char = testcase.split(",")
                correct = get_correct(word, char)
            
                cor_len = len(correct.split("\n"))
                self.assertTrue(len(output) == 0, f"Ohjelmasi ei pitäisi tulostaa mitään syötteellä ({testcase}). Se kuitenkin tulostaa \n{output_all}")

if __name__ == '__main__':
    unittest.main()
