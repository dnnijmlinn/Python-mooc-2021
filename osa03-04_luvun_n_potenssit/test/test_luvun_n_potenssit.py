import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.luvun_n_potenssit'

@points('3.luvun_n_potenssit')
class PotenssitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["3"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        with patch('builtins.input', side_effect = ["3", "3"]):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä 3 3")

    def test_1(self):
        for raja, kerroin in [(10, 3), (27, 3),(64, 4) ,(47, 3), (30, 5), (150, 7),  (200, 7),  (1000, 11),  (2000, 21)]:
            with patch('builtins.input', side_effect=[str(raja), str(kerroin), AssertionError("Syötettä pyydetään liian monta kertaa.") ] ) as prompt:
                reload_module(self.module)
                output_all =  get_stdout()
                output = output_all.split('\n')  

                self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään syötteellä {raja}")
                
                rivit = []
                for i in range(0, raja):
                    if kerroin**i > raja: 
                        break

                    rivit.append(str(kerroin**i))

                rivit_str = '\n'.join(rivit)
                self.assertEqual(len(rivit), len(output), f"Ohjelmasi tulisi tulostaa {len(rivit)} riviä lukuja syötteellä {raja} {kerroin}, nyt se tulostaa {len(output)} riviä:\n{output_all}\nodotettu tulostus on\n{rivit_str}")

                inpt = str(raja)
                for i in range(0, raja):
                    if kerroin**i > raja: 
                        break
                    expected = str(kerroin**i)
                    rivit_str = '\n'.join(rivit)
                    self.assertEqual(expected, output[i], f"rivin {i+1} tulostus väärin kun syöte on {raja} {kerroin}\nohjelmasi pitäisi tulostaa:\n{rivit_str}\nohjelmasi tulosti\n{output_all}")         

    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")                
            if 'break' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
