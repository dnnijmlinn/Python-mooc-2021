import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.ruokailukustannukset'

@points('1.ruokailukustannukset')
class RuokailuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_0(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
             
            self.assertTrue(len(output)>0, 'Ohjelmasi ei tulosta mitään' )
            self.assertFalse(prompt.call_count < 2, 'Ohjelman tulee pyytää kolmea syötettä.')
            expected = "Päivässä 4.5 euroa"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä 4, 2.5 ja 21.5 tulostaa rivi \n{expected}\nohjelmasi tulostus oli\n{output}")
            expected = "Viikossa 31.5 euroa"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä 4, 2.5 ja 21.5 tulostaa rivi \n{expected}\nohjelmasi tulostus oli\n{output}")
            
    def test_1(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            
            self.assertFalse(prompt.call_count < 2, 'Ohjelman tulee pyytää kolmea syötettä.')
            expected = "Päivässä 4.5 euroa"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä 4, 2.5 ja 21.5 tulostaa rivi \n{expected}\nohjelmasi tulostus oli\n{output}")
            expected = "Viikossa 31.5 euroa"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä 4, 2.5 ja 21.5 tulostaa rivi\n{expected}\nohjelmasi tulostus oli\n{output}")
                        
    def test_2_lisatestit(self):
        testset = [
            [ '5', '3.5', '43.75', '8.75', '61.25'], 
            [ '1', '2.25', '15.25', '2.5', '17.5' ],
            [ '0', '0', '0', '0.0', '0.0' ],
        ]
        for a, b, c, d, w in testset:
            with patch('builtins.input', side_effect = [ a, b, c, AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                inputs = f"{a}, {b}, ja {c}"
                self.assertFalse(prompt.call_count < 3, 'Ohjelman tulee pyytää kolmea syötettä.')
                expected = f"Päivässä {d} euroa"
                self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä {inputs} tulostaa rivi\n{expected}\nohjelmasi tulostus oli\n{output}")
                expected = f"Viikossa {w} euroa"
                self.assertTrue(sanitize(expected) in sanitize(output), f"Ohjelman tulisi syötteillä {inputs} tulostaa rivi\n{expected}\nohjelmasi tulostus oli\n{output}")    

if __name__ == '__main__':
    unittest.main()
