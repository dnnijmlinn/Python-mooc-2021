import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from inspect import getsource

exercise = 'src.kahden_potenssit'

@points('3.kahden_potenssit')
class KahdenPotenssitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["3"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        with patch('builtins.input', side_effect = "3"):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä 3")

    def test_1(self):
        for luku in [3, 4, 5, 11, 16, 24, 35, 43, 57, 101,1021]:

            with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}")
                
                rivit = []
                for i in range(0, luku):
                    if 2**i > luku: 
                        break

                    rivit.append(str(2**i))

                self.assertEqual(len(rivit), len(output), f"Ohjelmasi tulisi tulostaa {len(rivit)} riviä lukuja syötteellä {luku}, nyt se tulostaa {len(output)} riviä:\n{output_all}")

                inpt = str(luku)
                for i in range(0, luku):
                    if 2**i > luku: 
                        break
                    expected = str(2**i)
                    rivit_str = '\n'.join(rivit)
                    self.assertEqual(expected, output[i], f"rivin {i+1} tulostus väärin kun syöte on {luku}\nohjelmasi pitäisi tulostaa:\n{rivit_str}\nohjelmasi tulosti\n{output_all}")
    
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")                
            if 'break' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
