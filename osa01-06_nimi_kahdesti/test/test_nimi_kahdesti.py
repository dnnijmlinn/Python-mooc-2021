import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.nimi_kahdesti'

@points('1.nimi_kahdesti')
class NimiKahdestiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_syotteen_tulostus_1(self):
        with patch('builtins.input', return_value = 'Pekka'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Ohjelmasi ei tulosta mitään!")
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Pekka' and splitted[1].rstrip() == 'Pekka', f'Ohjelma ei toiminut oikein syötteellä: Pekka. Tulostit\n{output}\nOlisi pitänyt tulostaa\nPekka\nPekka')

    def test_syotteen_tulostus_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Ada' and splitted[1].rstrip() == 'Ada', f'Ohjelma ei toiminut oikein syötteellä: Ada. Tulostit\n{output}\nOlisi pitänyt tulostaa\Ada\Ada')


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
