import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap

exercise = 'src.palindromit'
function = 'palindromi'

def get_correct(test_case: list) -> list:
    pass


@points('4.palindromit')
class PalindromitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["aa"]):
           cls.module = load_module(exercise, 'fi')

    def test_5_syotteet2(self):
        test_cases = "eka toka kolmas neljas saippuakauppias".split()
        correct = ["ei ollut palindromi"] * 4
        correct.append("saippuakauppias on palindromi!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ") for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)
            ntest_cases = '\n'.join(test_cases)
            self.assertTrue(correct == output, f"Tuloste\n{noutput}\nei vastaa mallivastausta:\n{ncorrect}\nseuraavalla testisyötteellä:\n{ntest_cases}")

    def test_6_syotteet3(self):
        test_cases = "aaabaa bbbcb ccccdccc xyzzzxyz abcdcba".split()
        correct = ["ei ollut palindromi"] * 4
        correct.append("abcdcba on palindromi!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ")  for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)
            ntest_cases = '\n'.join(test_cases)    
            self.assertTrue(correct == output, f"Tuloste\n{noutput}\nei vastaa mallivastausta\n{ncorrect}\nseuraavalla testisyötteellä:\n{ntest_cases}")
                 
if __name__ == '__main__':
    unittest.main()
