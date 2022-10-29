import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.laskin'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.laskin')
class LaskinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_summa1(self):
        with patch('builtins.input', side_effect = [ '1', '2', 'summa', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '1 + 2 = 3'
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään syötteillä 1, 2, summa")
            self.assertTrue(expect in output, f"Syötteillä 1, 2, summa ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")

    def test_summa2(self):
        with patch('builtins.input', side_effect = [ '75', '23', 'summa', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään syötteillä 75, 23, summa")
            expect = '75 + 23 = 98'
            self.assertTrue(expect in output, f"Syötteillä 75, 23, summa ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")

    def test_erotus1(self):
        with patch('builtins.input', side_effect = [ '2', '1', 'erotus', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään syötteillä 2, 1, erotus")
            expect = '2 - 1 = 1'
            self.assertTrue(expect in output, f"Syötteillä 2, 1, erotus ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")

    def test_erotus2(self):
        with patch('builtins.input', side_effect = [ '13', '34', 'erotus', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '13 - 34 = -21'
            self.assertTrue(expect in output, f"Syötteillä 13, 34, erotus ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")

    def test_tulo1(self):
        with patch('builtins.input', side_effect = [ '2', '3', 'tulo', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '2 * 3 = 6'
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään syötteillä 2, 3, tulo")
            self.assertTrue(expect in output, f"Syötteillä 2, 3, tulo ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")
   
    def test_tulo2(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'tulo', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '27 * -3 = -81'
            self.assertTrue(expect in output, f"Syötteillä 27, -3, tulo ohjelmasi olisi pitänyt tulostaa\n{expect}\nOhjelmasi tulosti:\n{output}")

    def test_xcrap(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'osamaara', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) == 0, f"Syötteillä 27, -3, osamaara ohjelmasi ei olisi pitänyt tulostaa mitään\nOhjelmasi tulosti:\n{output}")

if __name__ == '__main__':
    unittest.main()
