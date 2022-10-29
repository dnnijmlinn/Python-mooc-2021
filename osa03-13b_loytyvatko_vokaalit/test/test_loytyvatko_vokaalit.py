import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.loytyvatko_vokaalit'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.loytyvatko_vokaalit')
class LoytyvatkoVokaalitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['a']):
            cls.module = load_module(exercise, 'fi')

    def test_jonot(self):
        values = ["hei", "hai","hoi", "heippa", "poppi", "puimuri", "kolea", "koppa", "keko"]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = [x + " löytyy"  if (x in test_case) else (x + " ei löydy") for x in "aeo"]
                self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on: {test_case}")
                r = 1
                for l1,l2 in zip(cor, output_list):
                    self.assertEqual(l1.strip(), l2.strip(), 
                        f"Tulostus väärin rivillä {r}: ohjelman pitäisi tulostaa\n{l1}\nmutta se tulostaa\n{l2}\nkun syöte on {test_case}")
                    r += 1
                
if __name__ == '__main__':
    unittest.main()
