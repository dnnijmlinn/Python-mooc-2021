import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.opiskelijat_ryhmiin'

@points('1.opiskelijat_ryhmiin')
class OpiskelijatRyhmiinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '1'):
            cls.module = load_module(exercise, 'fi')

    def test_A_8_ja_4(self):
        with patch('builtins.input', side_effect = [ '8', '4', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'Ohjelman tulee pyytää kahta syötettä.')
            expected = "Ryhmien määrä: 2"
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään")
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 8 ja 4 ohjelmasi tulisi tulostaa:\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            
    def test_B_11_ja_3(self):
        with patch('builtins.input', side_effect = [ '11', '3', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Ryhmien määrä: 4"
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 11 ja 3 ohjelmasi tulisi tulostaa:\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))

    def test_C_200_ja_99(self):
        with patch('builtins.input', side_effect = [ '200', '99', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Ryhmien määrä: 3"
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 200 ja 99 ohjelmasi tulisi tulostaa:\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            
    def test_D_53_ja_11(self):
        with patch('builtins.input', side_effect = [ '53', '11', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Ryhmien määrä: 5"
            self.assertTrue(sanitize(expected) in sanitize(output), "Syötteillä 53 ja 11 ohjelmasi tulisi tulostaa:\n{}\nohjelmasi tulostus oli\n{}".format(expected, output))
            
if __name__ == '__main__':
    unittest.main()
