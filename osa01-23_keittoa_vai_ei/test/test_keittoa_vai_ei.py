import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.keittoa_vai_ei'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

def oikea_jarjestys(output):
    parts = output.split("\n")
    hinta = False
    for part in parts:
        if 'Kokonaishinta on' in part:
            hinta = True
        if "Seuraava!" == part and not hinta:
            return False

    return True  

@points('1.keittoa_vai_ei')
class KeittoaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_kramer_1(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '1', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Seuraava!"
            self.assertTrue(len(output)>0, f"Ohjelmasi ei tulosta mitään")
            self.assertTrue(expected in output, f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 5.9'
            self.assertTrue(expected in output, f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n'Seuraava' vasta hinnan ilmoittamisen jälkeen\nohjelmasi tulosti\n"+ output)

    def test_2_kramer_4(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '4', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 23.6'
            self.assertTrue(expected in output, f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n'Seuraava' vasta hinnan ilmoittamisen jälkeen\nohjelmasi tulosti\n"+ output)

    def test_3_jerry(self):
        with patch('builtins.input', side_effect = [ 'Jerry', AssertionError("Syötettä pyydetään liian monta kertaa kun nimeksi ilmoitetaan Jerry.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Jerry ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)

    def test_4_jane_doe(self):
        with patch('builtins.input', side_effect = [ 'Jane Doe', '2', AssertionError("Syötettä pyydetään liian monta kertaa kun nimeksi ilmoitetaan Jane Doe.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Jane Doe, 2 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 11.8'
            self.assertTrue(expected in output, f"Syötteellä Jane Doe, 2 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)

if __name__ == '__main__':
    unittest.main()
