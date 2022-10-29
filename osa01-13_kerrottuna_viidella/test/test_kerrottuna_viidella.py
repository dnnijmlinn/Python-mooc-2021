import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.kerrottuna_viidella'

@points('1.kerrottuna_viidella')
class KerrottunaViidellaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kerrottuna_kolmella(self):
        with patch('builtins.input', return_value = '3'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Ohjelmasi ei tulosta mitään' )
            self.assertTrue('15' in output, 'Tulostus väärin syötteellä 3, ohjelmasi tulostaa\n' + output)
            expected = 'Kun kerrotaan 3 luvulla 5, saadaan 15'
            assert_ignore_ws(self, output, expected,  'Ohjelmasi tulostus ei ole oikea syötteellä 3, ')

    def test_kerrottuna_viidella(self):
        with patch('builtins.input', return_value = '5'):
            reload_module(self.module)
            output = get_stdout()
            expected = 'Kun kerrotaan 5 luvulla 5, saadaan 25'
            assert_ignore_ws(self, output, expected,  'Ohjelmasi tulostus ei ole oikea syötteellä 5, ')

    def test_kerrottuna_sadalla(self):
        with patch('builtins.input', return_value = '100'):
            reload_module(self.module)
            output = get_stdout()
            expected = 'Kun kerrotaan 100 luvulla 5, saadaan 500'
            assert_ignore_ws(self, output, expected,  'Ohjelmasi tulostus ei ole oikea syötteellä 100, ')

    def test_lukua_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '0') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Syötettä tulee pyytää täsmälleen kerran.')

if __name__ == '__main__':
    unittest.main()
