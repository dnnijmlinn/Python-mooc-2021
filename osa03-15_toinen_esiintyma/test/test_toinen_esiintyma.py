import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.toinen_esiintyma'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower().replace("  ", " ") == str2.lower().replace("  ", " ")

def get_correct(s : str, s2: str) -> str:
    if s.find(s2) > -1:
        return s.find(s2, s.find(s2) + len(s2))
    else:
        return -1

def f(m):
    return "\n".join(m.split(","))

@points('3.toinen_esiintyma')
class ToinenEsiintymaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = ["abcdabcdabcd","abc"]):
           cls.module = load_module(exercise, 'fi')

    def test_loytyy_2_tai_useampi(self):
        words = "abcdabcdabcd,abc erkkiesimerkki,erkki appilanpappilan,appi ac/dc,c ToBeOrNotToBe,Be hölkynkölkyn,ölky abababa,aba".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Varmista että ohjelma toimii syötteellä " + word)  
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                
                correct = get_correct(word, char)
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  +  f(testcase))  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, 1, len(output), output_all))
                
                self.assertTrue(str(correct) in output_all, "Tulosteesta ei löydy oikeaa vastausta {} kun syöte on\n{}\nOhjelma tulosti:\n{}". 
                    format(correct, f(testcase), output_all))

                correct_str = "Osajonon toinen esiintymä on kohdassa " + str(correct) + "."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct_str, testcase))

    def test_loytyy_vain_1(self):
        words = "nakkila,nak abcdabcd,bcda abracadabra,cad tsuppiduppi,uppid".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Varmista että ohjelma toimii syötteellä " +  f(testcase))  
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  +  f(testcase))  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, 1, len(output), output_all))
                
                correct_str = "Osajono ei esiinny merkkijonossa kahdesti."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct_str, testcase))

    def test_ei_loydy_yhtaan(self):
        words = "esimerkki,jerk abcdabcd,abcde tyhjäätäynnä,nyhjää 123454321,3212".split(" ")
        for testcase in words:
            with patch('builtins.input', side_effect = testcase.split(",")):
                word,char = testcase.split(",")
                try:
                    reload_module(self.module)
                except:
                    self.assertFalse(True, "Varmista että ohjelma toimii syötteellä " +  f(testcase))  
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä\n"+f(testcase))  
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, 1, len(output), output_all))
                
                correct_str = "Osajono ei esiinny merkkijonossa kahdesti."
                
                self.assertTrue(outputs_equal(output_all,  correct_str), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct_str, testcase))

if __name__ == '__main__':
    unittest.main()
