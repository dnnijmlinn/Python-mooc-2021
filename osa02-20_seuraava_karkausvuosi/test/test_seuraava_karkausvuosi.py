import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce
from random import randint

exercise = 'src.seuraava_karkausvuosi'

@points('20.seuraava_karkausvuosi')
class SeuraavaKarkausvuosiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["4321"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_2019(self):
        with patch('builtins.input', side_effect= ["2019", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()  

            expected = 'Vuotta 2019 seuraava karkausvuosi on 2020'
            self.assertFalse(len(output) == 0 , f"Syötteellä 2019 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi ei tulostanut mitään" )
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n2019ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_2020(self):
        with patch('builtins.input', side_effect= ["2020", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()

            self.assertFalse(len(output) == 0 , f"Ohjelmasi ei tulostanut mitään syötteellä 2024" )
            expected = 'Vuotta 2020 seuraava karkausvuosi on 2024'
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n2020\1ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_1896(self):
        with patch('builtins.input', side_effect= ["1896", AssertionError("Syötettä pyydetään liian monta kertaa.") ], ) as prompt:
            reload_module(self.module)
            output = get_stdout()

            self.assertFalse(len(output) == 0 , f"Ohjelmasi ei tulostanut mitään syötteellä 1896" )

            expected = 'Vuotta 1896 seuraava karkausvuosi on 1904'
            self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n1896\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_neljalla_jaolliset(self):
        values = "4 16 1204 1616 1976 2008".split(" ")
        for value in values:
            acual_value = int(value) - 3
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()
                expected = f'Vuotta {acual_value} seuraava karkausvuosi on {acual_value+3}'
                self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{acual_value}\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_sadalla_ei_400_jaolliset(self):
        values = "500 700 1100 1300 1900".split(" ")
        for value in values:
            acual_value = int(value) - 2
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()
                expected = f'Vuotta {acual_value} seuraava karkausvuosi on {acual_value+6}'
                self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{acual_value}\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )

    def test_neljallasadalla_jaolliset(self):
        values = "400 800 1600 2000 2400".split(" ")
        for value in values:
            acual_value = int(value) - 2
            with patch('builtins.input', return_value = str(acual_value)):
                reload_module(self.module)
                output = get_stdout()

                expected = f'Vuotta {acual_value} seuraava karkausvuosi on {acual_value+2}'
                self.assertEqual(sanitize(expected), sanitize(output), f"Syötteellä\n{acual_value}\nohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n{output}" )
    

if __name__ == '__main__':
    unittest.main()
