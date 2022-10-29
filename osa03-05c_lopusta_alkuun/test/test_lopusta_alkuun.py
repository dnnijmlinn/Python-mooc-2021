import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.lopusta_alkuun'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.lopusta_alkuun')
class LopustaAlkuunTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a']):
            cls.module = load_module(exercise, 'fi')

    def test_jonot(self):
        values = ["abc", "heippa", "apina", "testijono", "ohjelmointi"]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                try:
                    reload_module(self.module)
                except:
                     self.assertTrue(False, f"varmista että ohjelmasi toimii syötteellä {test_case}")
                output = get_stdout()
                output_list = output.split("\n")
                cor = [x for x in test_case[::-1]]
                self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä.")
                r = 1
                for l1,l2 in zip(cor, output_list):
                    self.assertTrue(sanitize(l1) == sanitize(l2), f"Kun syöte on {test_case} tulostus on väärin rivillä {r+1}, rivin pitäisi olla\n{l1}\nmutta se on\n{l2}")
    
if __name__ == '__main__':
    unittest.main()
