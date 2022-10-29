import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce

exercise = 'src.kertomat'

def outputs_equal(str1 : str, str2 : str) -> bool:
    return sanitize(str1.lower()) == sanitize(str2.lower())

def get_correct(s : list) -> str:
    s = [int(n) for n in s]
    ss = "\n".join(["Luvun " + str(i) + " kertoma on " + str(reduce(lambda a,b: a * b, range(1, i + 1 ))) for i in s if i > 0])
    return ss + "\n" + "Kiitos ja moi!"

def f(tc):
    return '\n'+'\n'.join(tc.split(' '))+'\n'
 
@points('3.kertomat')
class KertomatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["1", "0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_pysähtyy(self):
        with patch('builtins.input', side_effect = ['1', '0' , AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma pysähtyy syötteellä \n1\n0")
        with patch('builtins.input', side_effect = ['1', '-1' , AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma pysähtyy syötteellä \n1\n-1")
        with patch('builtins.input', side_effect = ['1', '-451' , AssertionError("Syötettä pyydetään liian monta kertaa.")]):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma pysähtyy syötteellä \n1\n-451")

    def test_2_lukuja(self):
        testcases = ["3 0", "2 4 6 5 -1", "1 2 3 7 6 -10", "5 4 3 8 0", "2 -1", "9 8 10 11 0"]
        for testcase in testcases:
            with patch('builtins.input', side_effect = testcase.split(" ")):
                reload_module(self.module)
                output_all = get_stdout().replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
                output = [x.strip() for x in output_all.split("\n") if len(x.strip()) > 0]
                correct = get_correct(testcase.split(" "))
                len_correct = len(correct.split("\n"))
            
                self.assertFalse(len(output_all)==0, "Ohjelmasi ei tulosta mitään syötteellä:\n"  + f(testcase)) 

                self.assertTrue(len(output) == len_correct, "Ohjelmasi tulostaa syötteellä {}{} rivin sijasta {} riviä: \n{}".
                    format(f(testcase), len_correct, len(output), output_all))
                
                self.assertTrue(outputs_equal(output_all, correct), 
                    "Ohjelmasi tuloste\n{}\nei vastaa oikeaa tulostetta \n{} \nsyötteellä:{}".
                    format(output_all, correct, f(testcase)))

if __name__ == '__main__':
    unittest.main()
