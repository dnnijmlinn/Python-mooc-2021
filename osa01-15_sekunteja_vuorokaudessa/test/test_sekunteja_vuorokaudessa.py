import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.sekunteja_vuorokaudessa'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.sekunteja_vuorokaudessa')
class SekuntejaVuorokaudessaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_yhden_vuodokauden_sekunnit(self):
        with patch('builtins.input', return_value = '1'):
            reload_module(self.module)
            result = get_stdout()
            self.assertTrue(len(result)>0, 'Ohjelmasi ei tulosta mitään' )
            self.assertTrue('86400' in result.split(), '1 vuorokaudessa tulisi olla 86400 sekuntia. Ohjelmasi tulosti: ' + parse_result(result))

    def test_2_seitseman_vuorokauden_sekunnit(self):
        with patch('builtins.input', return_value = '7'):
            reload_module(self.module)
            result = get_stdout()
            self.assertTrue('604800' in result.split(), '7 vuorokaudessa tulisi olla 604800 sekuntia. Ohjelmasi tulosti: ' + parse_result(result))

    def test_3_lisatestit(self):
        testset = [
            ['0', '0'],
            ['13', '1123200'],
            ['51', '4406400'],
            ['110', '9504000'],
            ['2020', '174528000']
        ]
        for vuorokaudet, sekunnit in testset:
            with patch('builtins.input', return_value = vuorokaudet):
                reload_module(self.module)
                self.assertTrue(sekunnit in get_stdout().split(), 'Ohjelmasi toimii väärin syötteellä ' + vuorokaudet + '. Vastauksen tulisi olla ' + sekunnit)

if __name__ == '__main__':
    unittest.main()
