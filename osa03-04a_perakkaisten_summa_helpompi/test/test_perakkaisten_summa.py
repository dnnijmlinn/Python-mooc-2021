import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from inspect import getsource

exercise = 'src.perakkaisten_summa'

@points('3.perakkaisten_summa_versio1')
class SummaTest(unittest.TestCase):
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
        for luku in [3, 4, 5, 6, 7, 8, 9, 10, 15, 21, 33]:

            with patch('builtins.input', side_effect=[str(luku), AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output =  get_stdout()

                self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään syötteellä {luku}")
                riveja = len(output.split('\n'))
                self.assertEqual(1, riveja, f"Ohjelmasi pitäisi tulosta ainoastaan 1 rivi, syötteellä {luku} se tulosti {riveja} riviä")

                asti = 1
                summa = 0
                while summa<luku:
                    summa += asti
                    asti += 1

                self.assertTrue(str(summa) in output, f"Tulostuksen pitäisi olla {summa} syötteellä {luku}. Ohjelmasi tulosti\n{output}")
 
    def test_2(self):
        source = getsource(self.module)
        for line in source.split("\n"):
            if 'while True' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")                
            if 'break' in line:
                self.assertTrue(False, f"tehtävää ei saa suorittaa while True -komennolla, eli koodistasi ei saa olla riviä\n{line}")

if __name__ == '__main__':
    unittest.main()
