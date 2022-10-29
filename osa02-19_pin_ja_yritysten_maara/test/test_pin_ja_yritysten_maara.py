import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.pin_ja_yritysten_maara'

def p(a):
    return "\n".join(a)

@points('2.pin_ja_yritysten_maara')
class PinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["4321"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        values = "4321".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä\n{}".format(p(values)))

    def test_1(self):
        with patch('builtins.input', side_effect= ["4321", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["4321"])

            expected = 'Oikein, tarvitsit vain yhden yrityksen!'
            self.assertFalse(len(output) == 0 , f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi ei tulostanut mitään" )
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

    def test_2(self):
        with patch('builtins.input', side_effect= ["1234", "4321", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["1234", "4321"])

            expected = 'Väärin\nOikein, tarvitsit 2 yritystä'
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

    def test_moar(self):
        for wrongs in [3, 4, 7, 11, 23]: 
            
            with patch('builtins.input', side_effect= ["0000"]* wrongs + ["4321", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  

                inpt = '\n'.join(["0000"]* wrongs + ["4321"]) 

                expected = '\n'.join(["Väärin"]*wrongs + ["Oikein, tarvitsit "+str(wrongs+1)+" yritystä"])
                self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

if __name__ == '__main__':
    unittest.main()
