import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.orwell'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.orwell')
class OrwellTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1984(self):
        with patch('builtins.input', return_value = '1984'):
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(len(output)==0, "Syötteellä 1984 ohjelman tulisi tulostaa Orwell\nohjelmasi ei tulostanut mitään")
            self.assertTrue('Orwell' in output, "Syötteellä 1984 ohjelman tulisi tulostaa Orwell\nohjelmasi tulosti\n" + output )

    def test_lisatestit(self):
        testset = ['2020', '1983', '1985']
        for vuosi in testset:
            with patch('builtins.input', return_value = vuosi):
                reload_module(self.module)
                output = get_stdout()
                self.assertFalse(len(output)>0, f"Syötteellä {vuosi} ohjelman ei pitäisi tulostaa mitään, ohjelmasi kuitenkin tulosti\n"+ output)

if __name__ == '__main__':
    unittest.main()
