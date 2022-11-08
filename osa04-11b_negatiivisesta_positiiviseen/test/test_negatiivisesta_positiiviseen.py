import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.negatiivisesta_positiiviseen'

@points('4.negatiivisesta_positiiviseen')
class NegatiivisestaPositiiviseenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["1"]):
            cls.module = load_module(exercise, 'fi')

    def test_syotteet(self):
        values = "2 3 7 5".split()
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = [str(x) for x in range(-(int(test_case)), int(test_case) + 1) if x != 0]

                mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
                """
                #\n{mssage}")   
                self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään kun syöte on {test_case}\n{mssage}")  
                self.assertEqual(len(output_list), len(cor), f"Ohjelmasi tulisi tulostaa syötteiden kysymisen lisäksi {len(cor)} riviä, nyt se tulostaa {len(output_list)} riviä kun syöte on {test_case}")
                r = 1
                for l1,l2 in zip(output_list, cor):
                    self.assertEqual(l1.strip(), l2, 
                        f"Ohjelmasi tulisi tulostaa rivillä {r} \n{l2} \nmutta nyt se tulostaa \n{l1}\nkun syöte on {test_case}")
                    r += 1

if __name__ == '__main__':
    unittest.main()
