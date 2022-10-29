import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.salasana_uudelleen'

@points('2.salasana_uudelleen')
class SalasanaUudelleenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["salainen"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0(self):
        values = "salainen salainen".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä {}".format(values))

    def test_1(self):
        with patch('builtins.input', side_effect= ["sekred", "sekred", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["sekred", "sekred"])

            expected = 'Käyttäjätunnus luotu!'
            self.assertFalse(len(output) == 0 , f"Syötteellä \n{inpt}\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi ei tulostanut mitään" )
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä \n{inpt}\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_2(self):
        with patch('builtins.input', side_effect= ["sekred", "wrong", "sekred", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            inpt = '\n'.join(["sekred", "wrong", "sekred"])

            expected = 'Ei ollut sama!\nKäyttäjätunnus luotu!'
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä \n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

    def test_moar(self):
        for wrongs in [3, 4, 7, 11, 23]: 
            
            with patch('builtins.input', side_effect= ["sekred"] + ["wrong"]* wrongs + ["sekred", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
                reload_module(self.module)
                output = get_stdout()  

                inpt = '\n'.join(["sekred"] + ["wrong"]* wrongs + ["sekred"]) 

                expected = '\n'.join(["Ei ollut sama!"]*wrongs + ["Käyttäjätunnus luotu!"])
                self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä \n{inpt}\nohjelmasi pitäisi tulostaa:\n{expected}\nohjelmasi tulosti:\n{output}" )

if __name__ == '__main__':
    unittest.main()
