import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.lahtolaskenta'

@points('3.lahtolaskenta')
class LahtolaskentaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[1] + ["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        with patch('builtins.input', side_effect = "2"):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä 2")

    def test_1(self):
        for luku in [3, 4, 5, 7, 9, 11, 21, 100]:

            with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}")
                self.assertEqual(luku+2, len(output), f"Ohjelmasi tulisi tulostaa {luku+2} riviä lukuja syötteellä {luku}, nyt se tulostaa {len(output)} riviä:\n{output_all}")

                self.assertEqual("Valmiina?", output[0], f"ensimmäisen tulostettavan rivin pitäisi olla \nValmiina?\nse on:\nV{output[0]}")
                self.assertEqual("Nyt!", output[len(output)-1], f"viimeisen tulostettavan rivin pitäisi olla\nNyt!\nse on:{output[len(output)-1]}")

                for i in range(1, luku+1):
                    self.assertEqual(str(luku-i+1), output[i], f"rivin {i+1} tulostus väärin kun syöte on {luku}\ohjelmasi tulostaa:\n{output_all}")
    
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")                
            if 'break' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")





if __name__ == '__main__':
    unittest.main()
