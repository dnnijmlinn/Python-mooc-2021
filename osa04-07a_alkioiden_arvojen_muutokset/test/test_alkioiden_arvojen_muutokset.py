import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.alkioiden_arvojen_muutokset'

def f(d):
    return '\n'.join(d)

def getcor(l):
    ls = list(range(1, 6))
    i = 0
    s = []
    while l[i] != -1:
        ls[l[i]] = l[i+1]
        i += 2
        s.append(str(ls))
    return s


@points('4.alkoiden_arvojen_muutokset')
class AlkioidenArvojenMuutoksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["-1"]):
            cls.module = load_module(exercise, 'fi')

    def test_syotteet1(self):
        values = (0,100,-1)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
            """
            #\n{mssage}") 

            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään kun syöte on {values}\n{mssage}") 
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on: {values}")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1.strip(), l2.strip(), 
                    f"Tulostus väärin rivillä {r}: ohjelman pitäisi tulostaa\n{l1}\nmutta se tulostaa\n{l2}\nkun syöte on {values}")
                r += 1

    def test_syotteet2(self):
        values = (1,25,3,333,2,-543,-1)
        with patch('builtins.input', side_effect = [str(x) for x in values]):
            reload_module(self.module)
            output = get_stdout()
            output_list = output.split("\n")
            cor = getcor(values)
            self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on: {values}")
            r = 1
            for l1,l2 in zip(cor, output_list):
                self.assertEqual(l1.strip(), l2.strip(), 
                    f"Tulostus väärin rivillä {r}: ohjelman pitäisi tulostaa\n{l1}\nmutta se tulostaa\n{l2}\nkun syöte on {values}")
                r += 1

if __name__ == '__main__':
    unittest.main()
