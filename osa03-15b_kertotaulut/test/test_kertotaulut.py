import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.kertotaulut'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('3.kertotaulut')
class KertotaulutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =['2']):
            cls.module = load_module(exercise, 'fi')

    def test_kertolaskut(self):
        values = [2, 3, 4]
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = []    
                for i in range(1, int(test_case) + 1):
                    for j in range(1, int(test_case) + 1):
                        cor.append(f"{i} x {j} = {i*j}")
                self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {test_case}.")
                r = 1
                cccc = "\n".join(cor)
                for l1,l2 in zip(cor, output_list):
                    self.assertTrue(sanitize(l1) == sanitize(l2), 
                        f"Tulostus ei ole oiken rivillä {r}: ohjelman pitäisi tulostaa\n{cccc}\nmutta se tulostaa \n{output}\nkun syöte on {test_case}")
                    r += 1

if __name__ == '__main__':
    unittest.main()