import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.parit_ympari'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return str1.lower() == str2.lower()

def get_correct(n : int) -> str:
    c1 = 2
    c2 = 1
    l = []

    while c1 <= n or c2 <= n:
        if c1 <= n:
            l.append(c1)
        if c2 <= n:
            l.append(c2)
        c1 += 2
        c2 += 2
    
    return "\n".join([str(x) for x in l])
    

@points('3.parit_ympari')
class ParitYmpariTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = "1"):
           cls.module = load_module(exercise, 'fi')


    def test_parittomat(self):
        testcases = "5 3 7 9 1 15".split()
        for testcase in testcases:
            with patch('builtins.input', return_value = testcase):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(int(testcase))
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + testcase) 

                self.assertTrue(len(output) == len_correct, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, len_correct, len(output), output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct, testcase))

    def test_parilliset(self):
        testcases = "2 6 8 12 4 18".split()
        for testcase in testcases:
            with patch('builtins.input', return_value = testcase):
                reload_module(self.module)
                output_all = get_stdout()
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(int(testcase))
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä "  + testcase) 

                self.assertTrue(len(output) == len_correct, "Ohjelmasi tulostaa syötteellä ({}) {} rivin sijasta {} riviä: \n{}".
                    format(testcase, len_correct, len(output), output_all))
                
                
                self.assertTrue(outputs_equal(output_all,  correct), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä ({})".
                    format(output_all, correct, testcase))
   
    

    
    
    

   
    


if __name__ == '__main__':
    unittest.main()
