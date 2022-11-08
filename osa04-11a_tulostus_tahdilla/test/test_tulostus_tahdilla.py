import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
from random import randint

exercise = 'src.tulostus_tahdilla'

@points('4.tulostus_tahdilla')
class TulostusTahdillaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["x"]):
            cls.module = load_module(exercise, 'fi')

    def test_syotteet(self):
        values = "hei testi pidempi abcd moikka ohjelmointitaito".split()
        for test_case in values:
            with patch('builtins.input', side_effect = [test_case]):
                reload_module(self.module)
                output = get_stdout()
                output_list = output.split("\n")
                cor = list("".join([x + "*" for x in test_case]))

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
