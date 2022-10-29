import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.itseisarvo'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.itseisarvo')
class ItseisarvoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_miinus_8(self):
        with patch('builtins.input', return_value = '-8'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('Luvun itseisarvo on 8' in output, "Syötteellä -8 ohjelmasi pitäisi tulostaa  \nLuvun itseisarvo on 8\nohjelmasi tulosti\n"+ output)

    def test_lisatestit(self):
        testset = ['-99', '4', '435634', '-234', '6', '0']
        for luku in testset:
            with patch('builtins.input', return_value = luku):
                reload_module(self.module)
                result = luku[1:-1] if int(luku)<0 else luku
                self.assertTrue(result in get_stdout(), 'Ohjelmasi toimii väärin syötteellä ' + luku + '. Vastauksen tulisi olla ' + result)

if __name__ == '__main__':
    unittest.main()
