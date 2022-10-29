import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.nimi_ja_huutomerkit'

@points('1.nimi_ja_huutomerkit')
class NimiJaHuutomerkkiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_syotteen_tulostus_1(self):
        with patch('builtins.input', return_value = 'Pekka'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään!")
            assert_ignore_ws(self, output, '!Pekka!Pekka!', 'Ohjelma ei toimi oikein syötteellä: Pekka\n' )

    def test_syotteen_tulostus_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            assert_ignore_ws(self,output, '!Ada!Ada!', 'Ohjelma ei toimi oikein syötteellä: Ada\n' )

    def test_syotetta_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Syötettä tulee pyytää täsmälleen kerran.')

if __name__ == '__main__':
    unittest.main()
